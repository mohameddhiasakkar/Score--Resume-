DOMAINS = {
    "auto": {
        "label": "Auto-detect field",
        "description": "Automatically identify your major from CV content",
        "icon": "sparkles",
    },
    "tech": {
        "label": "Computer Science & IT",
        "description": "Software, data, cloud, and engineering technology roles",
        "icon": "code",
    },
    "engineering": {
        "label": "Engineering",
        "description": "Mechanical, civil, electrical, and industrial engineering",
        "icon": "gear",
    },
    "healthcare": {
        "label": "Healthcare & Medicine",
        "description": "Nursing, medicine, pharmacy, and clinical care",
        "icon": "health",
    },
    "business": {
        "label": "Business & Finance",
        "description": "Management, accounting, marketing, and finance",
        "icon": "chart",
    },
    "law": {
        "label": "Law & Legal",
        "description": "Legal practice, compliance, and paralegal work",
        "icon": "scale",
    },
    "education": {
        "label": "Education & Teaching",
        "description": "Teaching, training, and academic roles",
        "icon": "book",
    },
    "science": {
        "label": "Science & Research",
        "description": "Laboratory research, biology, chemistry, and physics",
        "icon": "flask",
    },
    "design": {
        "label": "Arts & Design",
        "description": "Graphic design, UX, fashion, and creative production",
        "icon": "palette",
    },
    "hospitality": {
        "label": "Hospitality & Tourism",
        "description": "Hotels, restaurants, events, and travel services",
        "icon": "hotel",
    },
    "architecture": {
        "label": "Architecture & Construction",
        "description": "Building design, construction management, and BIM",
        "icon": "building",
    },
    "social": {
        "label": "Psychology & Social Work",
        "description": "Counseling, social services, and community support",
        "icon": "heart",
    },
    "media": {
        "label": "Media & Communications",
        "description": "Journalism, PR, broadcasting, and content creation",
        "icon": "mic",
    },
    "agriculture": {
        "label": "Agriculture & Environment",
        "description": "Farming, sustainability, forestry, and environmental science",
        "icon": "leaf",
    },
    "general": {
        "label": "General Professional",
        "description": "Cross-industry skills for any career path",
        "icon": "briefcase",
    },
}

SELECTABLE_DOMAINS = [key for key in DOMAINS if key != "auto"]

DOMAIN_SUMMARIES = {
    "tech": "technology and software",
    "engineering": "engineering and technical design",
    "healthcare": "healthcare and patient care",
    "business": "business and finance",
    "law": "legal and compliance",
    "education": "education and teaching",
    "science": "scientific research",
    "design": "creative and design",
    "hospitality": "hospitality and service",
    "architecture": "architecture and construction",
    "social": "social services and counseling",
    "media": "media and communications",
    "agriculture": "agriculture and environment",
    "general": "professional",
}
