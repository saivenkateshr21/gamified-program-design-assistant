PROGRAM_STAGES = {
    "Problem": {
        "title": "Problem Definition",
        "description": "Define the core problem you are trying to solve.",
        "steps": [
            {
                "key": "problem_statement",
                "label": "Core Problem Statement",
                "help": "What is the primary issue? (e.g., 'Low student attendance in rural schools')",
                "placeholder": "Enter the core problem clearly...",
                "type": "text_area"
            },
            {
                "key": "root_causes",
                "label": "Root Causes",
                "help": "Why does this problem exist? List the main reasons.",
                "placeholder": "1. Lack of transport\n2. Poor infrastructure...",
                "type": "text_area"
            },
            {
                "key": "target_group_problem",
                "label": "Who is most affected?",
                "help": "e.g., Students aged 6-14, Teachers in Zone A",
                "placeholder": "Describe the affected group...",
                "type": "text_input"
            }
        ]
    },
    "Outcomes": {
        "title": "Outcomes Identification",
        "description": "What changes do you expect to see?",
        "steps": [
            {
                "key": "short_term_outcomes",
                "label": "Short-term Outcomes (0-6 months)",
                "help": "Immediate changes (e.g., 'Teachers start using the new app')",
                "placeholder": "List short-term outcomes...",
                "type": "text_area"
            },
            {
                "key": "long_term_outcomes",
                "label": "Long-term Outcomes (1-3 years)",
                "help": "Lasting impact (e.g., '20% improvement in literacy rates')",
                "placeholder": "List long-term outcomes...",
                "type": "text_area"
            }
        ]
    },
    "Stakeholders": {
        "title": "Stakeholder Mapping",
        "description": "Who is involved in this program?",
        "steps": [
            {
                "key": "primary_stakeholders",
                "label": "Primary Stakeholders (Direct Beneficiaries)",
                "help": "Who directly benefits? (e.g., Students)",
                "placeholder": "List primary stakeholders...",
                "type": "text_input"
            },
            {
                "key": "secondary_stakeholders",
                "label": "Secondary Stakeholders (Implementers/Influencers)",
                "help": "Who helps implement or influence? (e.g., Parents, School Leaders)",
                "placeholder": "List secondary stakeholders...",
                "type": "text_input"
            }
        ]
    },
    "Activities": {
        "title": "Activities & Interventions",
        "description": "What will you do to achieve the outcomes?",
        "steps": [
            {
                "key": "key_activities",
                "label": "Key Activities",
                "help": "List the main actions. (e.g., 'Conduct teacher training workshops')",
                "placeholder": "Describe the activities...",
                "type": "text_area"
            },
            {
                "key": "resources_needed",
                "label": "Resources Needed",
                "help": "What do you need? (e.g., Training material, Tablets, Hall)",
                "placeholder": "List required resources...",
                "type": "text_area"
            }
        ]
    },
    "Metrics": {
        "title": "Success Metrics",
        "description": "How will you measure success?",
        "steps": [
            {
                "key": "kpis",
                "label": "Key Performance Indicators (KPIs)",
                "help": "Quantifiable measures. (e.g., '% of teachers completing training')",
                "placeholder": "List your KPIs...",
                "type": "text_area"
            },
            {
                "key": "means_of_verification",
                "label": "Means of Verification",
                "help": "How will you collect data? (e.g., 'Surveys', 'App logs')",
                "placeholder": "Describe verification methods...",
                "type": "text_input"
            }
        ]
    }
}
