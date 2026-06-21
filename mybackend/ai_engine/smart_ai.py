from .domains import DOMAIN_SUMMARIES, DOMAINS, SELECTABLE_DOMAINS
from .skills import SKILLS, get_domain_skill_keys, get_skills_for_domain


def _skill_terms(skill_key, skill_data):
    terms = [skill_key.lower()]
    for alias in skill_data.get("aliases", []):
        terms.append(alias.lower())
    return terms


def _text_contains_term(text, term):
    return term in text


def match_skills_in_set(cv_text, skill_keys):
    text = cv_text.lower()
    found = []
    for skill_key in skill_keys:
        skill_data = SKILLS[skill_key]
        if any(_text_contains_term(text, term) for term in _skill_terms(skill_key, skill_data)):
            found.append(skill_key)
    return found


def detect_domain(cv_text):
    """Pick the domain with the strongest skill signal in the CV."""
    text = cv_text.lower()
    scores = {}

    for domain in SELECTABLE_DOMAINS:
        if domain == "general":
            continue
        domain_skills = get_domain_skill_keys(domain)
        if not domain_skills:
            continue
        matches = match_skills_in_set(text, domain_skills)
        scores[domain] = {
            "matches": len(matches),
            "ratio": len(matches) / len(domain_skills),
            "matched_skills": matches,
        }

    if not scores:
        return "general", []

    ranked = sorted(
        scores.items(),
        key=lambda item: (item[1]["matches"], item[1]["ratio"]),
        reverse=True,
    )
    best_domain, best_score = ranked[0]

    if best_score["matches"] == 0:
        return "general", ranked[:3]

    return best_domain, [
        {
            "domain": domain,
            "label": DOMAINS[domain]["label"],
            "matches": data["matches"],
            "ratio": round(data["ratio"] * 100, 1),
        }
        for domain, data in ranked[:3]
        if data["matches"] > 0
    ]


def resolve_domain(cv_text, requested_domain):
    if requested_domain and requested_domain not in ("auto", ""):
        if requested_domain not in DOMAINS:
            return requested_domain, [], False
        return requested_domain, [], False

    detected, candidates = detect_domain(cv_text)
    return detected, candidates, True


def get_analysis_skills(domain):
    """Domain skills plus universal general soft skills for richer scoring."""
    domain_skills = get_skills_for_domain(domain)
    general_skills = get_skills_for_domain("general")
    combined = {**general_skills, **domain_skills}
    return combined


def calculate_score(found_skills, all_skill_keys):
    if len(all_skill_keys) == 0:
        return 0
    return round((len(found_skills) / len(all_skill_keys)) * 100, 2)


def get_grade(score):
    if score >= 85:
        return "Excellent"
    if score >= 70:
        return "Strong"
    if score >= 50:
        return "Good"
    if score >= 30:
        return "Developing"
    return "Needs Work"


def group_by_category(skill_keys, domain):
    domain_catalog = get_analysis_skills(domain)
    categories = []
    seen_categories = []

    for skill_key, skill_data in domain_catalog.items():
        category = skill_data["category"]
        if category not in seen_categories:
            seen_categories.append(category)

    grouped = {category: [] for category in seen_categories}
    for skill_key, skill_data in domain_catalog.items():
        grouped[skill_data["category"]].append({
            "key": skill_key,
            "label": skill_data["label"],
            "matched": skill_key in skill_keys,
        })

    return [
        {"category": category, "skills": grouped[category]}
        for category in seen_categories
        if grouped[category]
    ]


def find_cross_domain_skills(cv_text, active_domain):
    text = cv_text.lower()
    hits = []
    for skill_key, skill_data in SKILLS.items():
        if skill_data["domain"] in (active_domain, "general"):
            continue
        if any(_text_contains_term(text, term) for term in _skill_terms(skill_key, skill_data)):
            hits.append({
                "key": skill_key,
                "label": skill_data["label"],
                "domain": skill_data["domain"],
                "domain_label": DOMAINS[skill_data["domain"]]["label"],
            })
    return hits[:8]


def build_summary(score, domain, auto_detected):
    field = DOMAIN_SUMMARIES.get(domain, "your field")
    prefix = f"Based on your {field} profile" if auto_detected else f"Evaluated against {DOMAINS[domain]['label']} standards"

    if score >= 70:
        return f"{prefix}, your CV demonstrates strong coverage of key competencies."
    if score >= 40:
        return f"{prefix}, your CV covers core areas with room to highlight more domain-specific skills."
    return f"{prefix}, focus on adding core skills and concrete examples to strengthen your profile."


def build_recommendations(missing_skills, score, domain):
    if not missing_skills:
        return [{
            "title": "Outstanding profile",
            "detail": "Your CV covers all tracked skills for this field. Add metrics, certifications, and project outcomes to stand out further.",
            "priority": "low",
            "category": DOMAINS[domain]["label"],
        }]

    items = []
    for skill_key in missing_skills[:5]:
        skill_data = SKILLS[skill_key]
        items.append({
            "title": f"Add {skill_data['label']}",
            "detail": (
                f"Include {skill_data['label']} with specific examples, tools used, "
                f"and measurable results relevant to {DOMAINS[domain]['label']} roles."
            ),
            "priority": "high" if score < 50 else "medium",
            "category": skill_data["category"],
        })
    return items
