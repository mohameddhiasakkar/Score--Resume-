from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction

from cvapp.models import Resume
from ai_engine.domains import DOMAINS, SELECTABLE_DOMAINS
from ai_engine.models import Analysis
from ai_engine.skills import SKILLS
from ai_engine.smart_ai import (
    build_recommendations,
    build_summary,
    calculate_score,
    find_cross_domain_skills,
    get_analysis_skills,
    get_grade,
    group_by_category,
    match_skills_in_set,
    resolve_domain,
)
from ai_engine.utils import extract_text


@api_view(['GET'])
def list_domains(request):
    domains = [
        {
            "id": "auto",
            "label": DOMAINS["auto"]["label"],
            "description": DOMAINS["auto"]["description"],
            "icon": DOMAINS["auto"]["icon"],
        },
        *[
            {
                "id": domain_id,
                "label": meta["label"],
                "description": meta["description"],
                "icon": meta["icon"],
            }
            for domain_id in SELECTABLE_DOMAINS
        ],
    ]
    return Response({"domains": domains, "count": len(domains) - 1})


@api_view(['POST'])
def analyze_resume(request, resume_id):
    try:
        resume = Resume.objects.get(id=resume_id)
    except Resume.DoesNotExist:
        return Response(
            {"error": f"Resume {resume_id} not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    requested_domain = request.data.get("domain", "auto")

    try:
        text = extract_text(resume.file)
        if not text or len(text.strip()) < 50:
            return Response(
                {"error": "Could not extract meaningful text from PDF. Try a text-based PDF export."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        domain, domain_candidates, auto_detected = resolve_domain(text, requested_domain)
        if domain not in DOMAINS:
            return Response(
                {"error": f"Unknown domain '{requested_domain}'. Use GET /api/domains/ for valid options."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        catalog = get_analysis_skills(domain)
        skill_keys = list(catalog.keys())
        found_skills = match_skills_in_set(text, skill_keys)
        found_set = set(found_skills)
        missing_skills = [key for key in skill_keys if key not in found_set]

        score = calculate_score(found_skills, skill_keys)
        grade = get_grade(score)
        recommendations = build_recommendations(missing_skills, score, domain)
        categories = group_by_category(found_set, domain)
        cross_domain = find_cross_domain_skills(text, domain)
        summary = build_summary(score, domain, auto_detected)

        with transaction.atomic():
            analysis, created = Analysis.objects.update_or_create(
                resume=resume,
                defaults={
                    "score": score,
                    "missing_skills": ", ".join(missing_skills),
                    "recommendations": recommendations[0]["detail"] if recommendations else "",
                },
            )

        return Response({
            "resume_id": resume.id,
            "filename": resume.file.name.split("/")[-1],
            "domain": domain,
            "domain_label": DOMAINS[domain]["label"],
            "auto_detected": auto_detected,
            "domain_candidates": domain_candidates,
            "score": score,
            "grade": grade,
            "summary": summary,
            "found_skills": [SKILLS[s]["label"] for s in found_skills],
            "missing_skills": [SKILLS[s]["label"] for s in missing_skills],
            "found_count": len(found_skills),
            "missing_count": len(missing_skills),
            "total_skills": len(skill_keys),
            "match_percentage": f"{score}%",
            "categories": categories,
            "cross_domain_skills": cross_domain,
            "recommendations": recommendations,
            "is_new_analysis": created,
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response(
            {"error": f"Analysis failed: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
