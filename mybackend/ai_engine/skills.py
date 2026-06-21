from .domains import SELECTABLE_DOMAINS

# Each skill: domain, category, label, optional aliases for matching
SKILLS = {
    # ── Computer Science & IT ──
    "python": {"domain": "tech", "category": "Programming", "label": "Python"},
    "javascript": {"domain": "tech", "category": "Programming", "label": "JavaScript"},
    "java": {"domain": "tech", "category": "Programming", "label": "Java"},
    "sql": {"domain": "tech", "category": "Data", "label": "SQL"},
    "react": {"domain": "tech", "category": "Frameworks", "label": "React"},
    "django": {"domain": "tech", "category": "Frameworks", "label": "Django"},
    "machine learning": {"domain": "tech", "category": "Data", "label": "Machine Learning"},
    "docker": {"domain": "tech", "category": "DevOps", "label": "Docker"},
    "aws": {"domain": "tech", "category": "Cloud", "label": "AWS"},
    "git": {"domain": "tech", "category": "DevOps", "label": "Git"},
    "cybersecurity": {"domain": "tech", "category": "Security", "label": "Cybersecurity"},
    "networking": {"domain": "tech", "category": "Infrastructure", "label": "Networking"},
    "agile": {"domain": "tech", "category": "Methodology", "label": "Agile"},
    "rest api": {"domain": "tech", "category": "Backend", "label": "REST API"},
    "data analysis": {"domain": "tech", "category": "Data", "label": "Data Analysis"},

    # ── Engineering ──
    "autocad": {"domain": "engineering", "category": "CAD Tools", "label": "AutoCAD"},
    "solidworks": {"domain": "engineering", "category": "CAD Tools", "label": "SolidWorks"},
    "matlab": {"domain": "engineering", "category": "Simulation", "label": "MATLAB"},
    "plc": {"domain": "engineering", "category": "Automation", "label": "PLC Programming"},
    "hvac": {"domain": "engineering", "category": "Mechanical", "label": "HVAC"},
    "structural analysis": {"domain": "engineering", "category": "Civil", "label": "Structural Analysis"},
    "quality control": {"domain": "engineering", "category": "Quality", "label": "Quality Control"},
    "lean manufacturing": {"domain": "engineering", "category": "Process", "label": "Lean Manufacturing"},
    "six sigma": {"domain": "engineering", "category": "Process", "label": "Six Sigma"},
    "technical drawing": {"domain": "engineering", "category": "Design", "label": "Technical Drawing"},
    "circuit design": {"domain": "engineering", "category": "Electrical", "label": "Circuit Design"},
    "project engineering": {"domain": "engineering", "category": "Management", "label": "Project Engineering"},
    "root cause analysis": {"domain": "engineering", "category": "Quality", "label": "Root Cause Analysis"},
    "gd&t": {"domain": "engineering", "category": "Mechanical", "label": "GD&T", "aliases": ["geometric dimensioning"]},

    # ── Healthcare & Medicine ──
    "patient care": {"domain": "healthcare", "category": "Clinical", "label": "Patient Care"},
    "cpr": {"domain": "healthcare", "category": "Clinical", "label": "CPR Certification"},
    "clinical research": {"domain": "healthcare", "category": "Research", "label": "Clinical Research"},
    "hipaa": {"domain": "healthcare", "category": "Compliance", "label": "HIPAA Compliance"},
    "medical terminology": {"domain": "healthcare", "category": "Knowledge", "label": "Medical Terminology"},
    "pharmacology": {"domain": "healthcare", "category": "Knowledge", "label": "Pharmacology"},
    "electronic health records": {"domain": "healthcare", "category": "Systems", "label": "EHR Systems", "aliases": ["ehr", "emr"]},
    "triage": {"domain": "healthcare", "category": "Clinical", "label": "Triage"},
    "wound care": {"domain": "healthcare", "category": "Clinical", "label": "Wound Care"},
    "infection control": {"domain": "healthcare", "category": "Safety", "label": "Infection Control"},
    "patient assessment": {"domain": "healthcare", "category": "Clinical", "label": "Patient Assessment"},
    "medical coding": {"domain": "healthcare", "category": "Administration", "label": "Medical Coding", "aliases": ["icd-10", "icd10"]},
    "telehealth": {"domain": "healthcare", "category": "Digital Health", "label": "Telehealth"},
    "laboratory techniques": {"domain": "healthcare", "category": "Lab", "label": "Laboratory Techniques"},

    # ── Business & Finance ──
    "financial analysis": {"domain": "business", "category": "Finance", "label": "Financial Analysis"},
    "accounting": {"domain": "business", "category": "Finance", "label": "Accounting"},
    "excel": {"domain": "business", "category": "Tools", "label": "Microsoft Excel", "aliases": ["microsoft excel", "spreadsheet"]},
    "budgeting": {"domain": "business", "category": "Finance", "label": "Budgeting"},
    "marketing strategy": {"domain": "business", "category": "Marketing", "label": "Marketing Strategy"},
    "sales": {"domain": "business", "category": "Sales", "label": "Sales"},
    "crm": {"domain": "business", "category": "Tools", "label": "CRM Software", "aliases": ["salesforce", "hubspot"]},
    "business development": {"domain": "business", "category": "Strategy", "label": "Business Development"},
    "market research": {"domain": "business", "category": "Marketing", "label": "Market Research"},
    "financial modeling": {"domain": "business", "category": "Finance", "label": "Financial Modeling"},
    "supply chain": {"domain": "business", "category": "Operations", "label": "Supply Chain Management"},
    "negotiation": {"domain": "business", "category": "Soft Skills", "label": "Negotiation"},
    "kpi": {"domain": "business", "category": "Analytics", "label": "KPI Tracking", "aliases": ["key performance indicator"]},
    "erp": {"domain": "business", "category": "Systems", "label": "ERP Systems", "aliases": ["sap", "oracle erp"]},

    # ── Law & Legal ──
    "legal research": {"domain": "law", "category": "Research", "label": "Legal Research"},
    "contract law": {"domain": "law", "category": "Practice Areas", "label": "Contract Law"},
    "litigation": {"domain": "law", "category": "Practice Areas", "label": "Litigation"},
    "compliance": {"domain": "law", "category": "Regulatory", "label": "Compliance"},
    "due diligence": {"domain": "law", "category": "Corporate", "label": "Due Diligence"},
    "legal writing": {"domain": "law", "category": "Communication", "label": "Legal Writing"},
    "case management": {"domain": "law", "category": "Administration", "label": "Case Management"},
    "intellectual property": {"domain": "law", "category": "Practice Areas", "label": "Intellectual Property", "aliases": ["patent", "trademark"]},
    "corporate law": {"domain": "law", "category": "Practice Areas", "label": "Corporate Law"},
    "regulatory affairs": {"domain": "law", "category": "Regulatory", "label": "Regulatory Affairs"},
    "mediation": {"domain": "law", "category": "Dispute Resolution", "label": "Mediation"},
    "legal drafting": {"domain": "law", "category": "Documentation", "label": "Legal Drafting"},
    "westlaw": {"domain": "law", "category": "Tools", "label": "Westlaw", "aliases": ["lexisnexis", "lexis nexis"]},

    # ── Education & Teaching ──
    "curriculum development": {"domain": "education", "category": "Instruction", "label": "Curriculum Development"},
    "classroom management": {"domain": "education", "category": "Instruction", "label": "Classroom Management"},
    "lesson planning": {"domain": "education", "category": "Instruction", "label": "Lesson Planning"},
    "student assessment": {"domain": "education", "category": "Evaluation", "label": "Student Assessment"},
    "special education": {"domain": "education", "category": "Specialization", "label": "Special Education"},
    "lms": {"domain": "education", "category": "Technology", "label": "Learning Management Systems", "aliases": ["moodle", "canvas", "blackboard"]},
    "differentiated instruction": {"domain": "education", "category": "Pedagogy", "label": "Differentiated Instruction"},
    "educational technology": {"domain": "education", "category": "Technology", "label": "Educational Technology", "aliases": ["edtech"]},
    "tutoring": {"domain": "education", "category": "Support", "label": "Tutoring"},
    "academic advising": {"domain": "education", "category": "Support", "label": "Academic Advising"},
    "instructional design": {"domain": "education", "category": "Design", "label": "Instructional Design"},
    "early childhood": {"domain": "education", "category": "Specialization", "label": "Early Childhood Education"},
    "higher education": {"domain": "education", "category": "Specialization", "label": "Higher Education"},

    # ── Science & Research ──
    "laboratory research": {"domain": "science", "category": "Research", "label": "Laboratory Research"},
    "statistical analysis": {"domain": "science", "category": "Analysis", "label": "Statistical Analysis"},
    "pcr": {"domain": "science", "category": "Lab Techniques", "label": "PCR", "aliases": ["polymerase chain reaction"]},
    "microscopy": {"domain": "science", "category": "Lab Techniques", "label": "Microscopy"},
    "chromatography": {"domain": "science", "category": "Lab Techniques", "label": "Chromatography"},
    "spectroscopy": {"domain": "science", "category": "Lab Techniques", "label": "Spectroscopy"},
    "grant writing": {"domain": "science", "category": "Academic", "label": "Grant Writing"},
    "peer review": {"domain": "science", "category": "Academic", "label": "Peer Review"},
    "spss": {"domain": "science", "category": "Tools", "label": "SPSS"},
    "r programming": {"domain": "science", "category": "Tools", "label": "R Programming", "aliases": [" r ", "r language"]},
    "field research": {"domain": "science", "category": "Research", "label": "Field Research"},
    "bioinformatics": {"domain": "science", "category": "Specialization", "label": "Bioinformatics"},
    "scientific writing": {"domain": "science", "category": "Communication", "label": "Scientific Writing"},

    # ── Arts & Design ──
    "photoshop": {"domain": "design", "category": "Creative Tools", "label": "Adobe Photoshop"},
    "illustrator": {"domain": "design", "category": "Creative Tools", "label": "Adobe Illustrator"},
    "figma": {"domain": "design", "category": "UX/UI", "label": "Figma"},
    "ui design": {"domain": "design", "category": "UX/UI", "label": "UI Design", "aliases": ["user interface"]},
    "ux research": {"domain": "design", "category": "UX/UI", "label": "UX Research", "aliases": ["user experience"]},
    "typography": {"domain": "design", "category": "Visual Design", "label": "Typography"},
    "branding": {"domain": "design", "category": "Visual Design", "label": "Branding"},
    "video editing": {"domain": "design", "category": "Production", "label": "Video Editing", "aliases": ["premiere pro", "final cut"]},
    "motion graphics": {"domain": "design", "category": "Production", "label": "Motion Graphics", "aliases": ["after effects"]},
    "3d modeling": {"domain": "design", "category": "3D", "label": "3D Modeling", "aliases": ["blender", "maya", "3ds max"]},
    "portfolio design": {"domain": "design", "category": "Presentation", "label": "Portfolio Design"},
    "color theory": {"domain": "design", "category": "Visual Design", "label": "Color Theory"},
    "wireframing": {"domain": "design", "category": "UX/UI", "label": "Wireframing"},

    # ── Hospitality & Tourism ──
    "customer service": {"domain": "hospitality", "category": "Service", "label": "Customer Service"},
    "event planning": {"domain": "hospitality", "category": "Events", "label": "Event Planning"},
    "food safety": {"domain": "hospitality", "category": "Compliance", "label": "Food Safety", "aliases": ["haccp", "servsafe"]},
    "hotel management": {"domain": "hospitality", "category": "Operations", "label": "Hotel Management"},
    "front desk operations": {"domain": "hospitality", "category": "Operations", "label": "Front Desk Operations"},
    "banquet service": {"domain": "hospitality", "category": "Food & Beverage", "label": "Banquet Service"},
    "tourism marketing": {"domain": "hospitality", "category": "Marketing", "label": "Tourism Marketing"},
    "reservation systems": {"domain": "hospitality", "category": "Systems", "label": "Reservation Systems", "aliases": ["opera pms"]},
    "guest relations": {"domain": "hospitality", "category": "Service", "label": "Guest Relations"},
    "revenue management": {"domain": "hospitality", "category": "Finance", "label": "Revenue Management"},
    "culinary arts": {"domain": "hospitality", "category": "Food & Beverage", "label": "Culinary Arts"},
    "travel coordination": {"domain": "hospitality", "category": "Operations", "label": "Travel Coordination"},

    # ── Architecture & Construction ──
    "revit": {"domain": "architecture", "category": "BIM", "label": "Autodesk Revit"},
    "bim": {"domain": "architecture", "category": "BIM", "label": "Building Information Modeling"},
    "construction management": {"domain": "architecture", "category": "Management", "label": "Construction Management"},
    "building codes": {"domain": "architecture", "category": "Regulations", "label": "Building Codes"},
    "site supervision": {"domain": "architecture", "category": "Field", "label": "Site Supervision"},
    "cost estimation": {"domain": "architecture", "category": "Finance", "label": "Cost Estimation", "aliases": ["quantity surveying"]},
    "sustainable design": {"domain": "architecture", "category": "Design", "label": "Sustainable Design", "aliases": ["leed", "green building"]},
    "architectural drafting": {"domain": "architecture", "category": "Design", "label": "Architectural Drafting"},
    "project scheduling": {"domain": "architecture", "category": "Management", "label": "Project Scheduling", "aliases": ["primavera", "ms project"]},
    "structural design": {"domain": "architecture", "category": "Engineering", "label": "Structural Design"},
    "surveying": {"domain": "architecture", "category": "Field", "label": "Surveying"},
    "contract administration": {"domain": "architecture", "category": "Management", "label": "Contract Administration"},

    # ── Psychology & Social Work ──
    "counseling": {"domain": "social", "category": "Clinical", "label": "Counseling"},
    "crisis intervention": {"domain": "social", "category": "Clinical", "label": "Crisis Intervention"},
    "case notes": {"domain": "social", "category": "Documentation", "label": "Case Documentation"},
    "mental health assessment": {"domain": "social", "category": "Clinical", "label": "Mental Health Assessment"},
    "cognitive behavioral": {"domain": "social", "category": "Therapy", "label": "CBT", "aliases": ["cbt", "cognitive behavioral therapy"]},
    "community outreach": {"domain": "social", "category": "Community", "label": "Community Outreach"},
    "child welfare": {"domain": "social", "category": "Specialization", "label": "Child Welfare"},
    "substance abuse": {"domain": "social", "category": "Specialization", "label": "Substance Abuse Counseling"},
    "group therapy": {"domain": "social", "category": "Therapy", "label": "Group Therapy"},
    "psychological testing": {"domain": "social", "category": "Assessment", "label": "Psychological Testing"},
    "social services": {"domain": "social", "category": "Community", "label": "Social Services"},
    "trauma-informed care": {"domain": "social", "category": "Clinical", "label": "Trauma-Informed Care"},

    # ── Media & Communications ──
    "journalism": {"domain": "media", "category": "Writing", "label": "Journalism"},
    "public relations": {"domain": "media", "category": "PR", "label": "Public Relations", "aliases": [" pr ", "press release"]},
    "content strategy": {"domain": "media", "category": "Digital", "label": "Content Strategy"},
    "social media management": {"domain": "media", "category": "Digital", "label": "Social Media Management"},
    "copywriting": {"domain": "media", "category": "Writing", "label": "Copywriting"},
    "broadcasting": {"domain": "media", "category": "Production", "label": "Broadcasting"},
    "media relations": {"domain": "media", "category": "PR", "label": "Media Relations"},
    "seo": {"domain": "media", "category": "Digital", "label": "SEO", "aliases": ["search engine optimization"]},
    "podcast production": {"domain": "media", "category": "Production", "label": "Podcast Production"},
    "storytelling": {"domain": "media", "category": "Creative", "label": "Storytelling"},
    "crisis communication": {"domain": "media", "category": "PR", "label": "Crisis Communication"},
    "audience analytics": {"domain": "media", "category": "Analytics", "label": "Audience Analytics"},

    # ── Agriculture & Environment ──
    "crop management": {"domain": "agriculture", "category": "Farming", "label": "Crop Management"},
    "soil analysis": {"domain": "agriculture", "category": "Science", "label": "Soil Analysis"},
    "irrigation systems": {"domain": "agriculture", "category": "Operations", "label": "Irrigation Systems"},
    "environmental impact": {"domain": "agriculture", "category": "Environment", "label": "Environmental Impact Assessment"},
    "sustainability": {"domain": "agriculture", "category": "Environment", "label": "Sustainability"},
    "wildlife conservation": {"domain": "agriculture", "category": "Conservation", "label": "Wildlife Conservation"},
    "gis mapping": {"domain": "agriculture", "category": "Tools", "label": "GIS Mapping", "aliases": [" geographic information", "arcgis", "qgis"]},
    "pest management": {"domain": "agriculture", "category": "Farming", "label": "Pest Management", "aliases": ["ipm", "integrated pest"]},
    "forestry": {"domain": "agriculture", "category": "Conservation", "label": "Forestry"},
    "water quality": {"domain": "agriculture", "category": "Environment", "label": "Water Quality Monitoring"},
    "organic farming": {"domain": "agriculture", "category": "Farming", "label": "Organic Farming"},
    "climate science": {"domain": "agriculture", "category": "Science", "label": "Climate Science"},

    # ── General Professional (cross-domain) ──
    "communication": {"domain": "general", "category": "Soft Skills", "label": "Communication"},
    "leadership": {"domain": "general", "category": "Soft Skills", "label": "Leadership"},
    "teamwork": {"domain": "general", "category": "Soft Skills", "label": "Teamwork"},
    "problem solving": {"domain": "general", "category": "Soft Skills", "label": "Problem Solving"},
    "time management": {"domain": "general", "category": "Soft Skills", "label": "Time Management"},
    "project management": {"domain": "general", "category": "Management", "label": "Project Management"},
    "presentation skills": {"domain": "general", "category": "Communication", "label": "Presentation Skills"},
    "critical thinking": {"domain": "general", "category": "Soft Skills", "label": "Critical Thinking"},
    "microsoft office": {"domain": "general", "category": "Tools", "label": "Microsoft Office", "aliases": ["ms office", "word", "powerpoint"]},
    "research": {"domain": "general", "category": "Academic", "label": "Research"},
    "report writing": {"domain": "general", "category": "Communication", "label": "Report Writing"},
    "bilingual": {"domain": "general", "category": "Language", "label": "Bilingual", "aliases": ["fluent in", "multilingual", "language skills"]},
}


def get_skills_for_domain(domain):
    if domain == "auto":
        return {}
    return {key: value for key, value in SKILLS.items() if value["domain"] == domain}


def get_domain_skill_keys(domain):
    return list(get_skills_for_domain(domain).keys())


def get_all_domain_categories(domain):
    categories = []
    seen = set()
    for skill in get_skills_for_domain(domain).values():
        cat = skill["category"]
        if cat not in seen:
            seen.add(cat)
            categories.append(cat)
    return categories
