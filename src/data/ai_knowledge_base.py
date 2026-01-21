
# Knowledge Base for Rule-Based AI Assistant
# This file contains the "brain" of the assistant: keywords, questions, and examples.

AI_KNOWLEDGE = {
    # --- EXPANDED KNOWLEDGE BASE ---
    "Problem": {
        "title": "Problem Definition",
        "defaults": {
            "questions": [
                "Who specifically is affected by this problem?",
                "What is the immediate impact of this problem on their daily lives?",
                "Is this a new problem or a long-standing one?"
            ],
            "examples": [
                "Example: 'High dropout rates among teenage girls in rural districts.'",
                "Example: 'Lack of access to clean drinking water causing recurrent illness.'"
            ]
        },
        "keywords": {
            "water": {
                "questions": [
                    "Is the water issue related to scarcity (quantity) or contamination (quality)?",
                    "How does the lack of water affect school attendance specifically?",
                    "Are there seasonal variations to this problem?"
                ],
                "examples": [
                    "Problem: 'Students miss school due to waterborne diseases from contaminated tap water.'",
                    "Root Cause: 'Broken filtration systems and lack of maintenance funds.'"
                ]
            },
            "school": {
                "questions": [
                    "Is the issue with the infrastructure, the curriculum, or the teaching quality?",
                    "How do parents currently perceive the school environment?",
                    "What specific grade levels are most affected?"
                ],
                "examples": [
                    "Problem: 'Grade 5 students have low reading comprehension levels.'",
                    "Root Cause: 'Teachers lack training in phonics-based instruction.'"
                ]
            },
            "health": {
                "questions": [
                    "Is this a preventative health issue or a treatment access issue?",
                    "How does this health issue impact economic productivity or education?",
                    "Are there cultural beliefs that influence this health behavior?"
                ],
                "examples": [
                    "Problem: 'Malnutrition in toddlers leading to stunted growth.'",
                    "Root Cause: 'Lack of awareness about affordable nutritious local foods.'"
                ]
            },
            "teacher": {
                "questions": [
                    "Are teachers lacking motivation, resources, or skills?",
                    "What is the current teacher-student ratio?",
                    "How are teachers currently supported or trained?"
                ],
                "examples": [
                    "Problem: 'High teacher absenteeism in remote village schools.'",
                    "Root Cause: 'Lack of safe housing and transport for teachers.'"
                ]
            },
            "transport": {
                "questions": [
                    "Is the lack of transport affecting students or teachers more?",
                    "Is it a cost issue or an availability issue?"
                ],
                "examples": [
                    "Problem: 'Girls drop out after 8th grade due to lack of safe transport to the high school.'",
                    "Root Cause: 'High school is 5km away and there is no bus service.'"
                ]
            },
            "money": {
                "questions": [
                    "Is the lack of funds due to low budget allocation or poor management?",
                    "Are families unable to afford school supplies?"
                ],
                "examples": [
                    "Problem: 'Parents cannot afford textbooks and uniforms.'",
                    "Root Cause: 'Economic hardship due to seasonal unemployment in the village.'"
                ]
            },
            "electricity": {
                "questions": [
                    "How frequent are power cuts?",
                    "Do you need a solar backup for digital classrooms?"
                ],
                "examples": [
                    "Problem: 'Computer lab is unusable 50% of the time due to power outages.'",
                    "Root Cause: 'Grid instability and lack of budget for diesel generators.'"
                ]
            },
             "power": {
                "questions": [
                    "How frequent are power cuts?",
                    "Do you need a solar backup for digital classrooms?"
                ],
                 "examples": [
                    "Problem: 'Computer lab is unusable 50% of the time due to power outages.'",
                    "Root Cause: 'Grid instability and lack of budget for diesel generators.'"
                ]
            },
            "gender": {
                "questions": [
                    "Are there cultural barriers specific to girls or boys?",
                    "Is safety a concern for this specific gender group?"
                ],
                "examples": [
                    "Problem: 'Girls stop attending after puberty due to lack of separate toilets.'",
                     "Root Cause: 'School infrastructure was built 20 years ago without gender sensitivity.'"
                ]
            },
            "girl": {
                "questions": [
                    "Are there cultural barriers specific to girls?",
                    "Is safety a concern for this specific gender group?"
                ],
                "examples": [
                    "Problem: 'Girls stop attending after puberty due to lack of separate toilets.'",
                     "Root Cause: 'School infrastructure was built 20 years ago without gender sensitivity.'"
                ]
            },
             "boy": {
                 "questions": [
                    "Are boys dropping out early for labor work?",
                    "Is behavioral discipline an issue?"
                ],
                "examples": [
                    "Problem: 'Boys leave school at 14 to work in the fields.'"
                ]
            }
        }
    },

    "Outcomes": {
        "title": "Outcomes Identification",
        "defaults": {
            "questions": [
                "What will be the first sign that things are improving?",
                "How will the beneficiaries' behavior change?",
                "Is this outcome realistic within the proposed timeframe?"
            ],
            "examples": [
                "Short-term: '80% of students attend school regularly for 3 months.'",
                "Long-term: 'Community takes full ownership of the water pump maintenance.'"
            ]
        },
        "keywords": {
            "awareness": {
                "questions": [
                    "Does awareness lead to action? How will you ensure behavior change follows?",
                    "How will you measure 'increased awareness'?"
                ],
                "examples": [
                    "Outcome: 'Parents actively participate in monthly school management meetings.' (Behavior, not just awareness)"
                ]
            },
            "skill": {
                "questions": [
                    "Will they be able to apply this skill independently?",
                    "What level of proficiency is expected?"
                ],
                "examples": [
                    "Outcome: 'Teachers confidently use the new reading kits in 90% of classes.'"
                ]
            },
             "attendance": {
                "questions": [
                    "What is the target attendance rate?",
                    "Will you measure daily average or individual regularity?"
                ],
                "examples": [
                    "Outcome: 'Reduce chronic absenteeism by 50% in the next academic year.'"
                ]
            }
        }
    },

    "Stakeholders": {
        "title": "Stakeholder Mapping",
        "defaults": {
            "questions": [
                "Are there any 'silent' stakeholders who are affected but have no voice?",
                "Who might oppose this project and why?",
                "Who are the key decision-makers you need to convince?"
            ],
            "examples": [
                "Primary: 'Students, Mothers'",
                "Secondary: 'School Principals, District Education Officers, Local Shopkeepers'"
            ]
        },
        "keywords": {
            "government": {
                "questions": [
                    "Which specific department or official is responsible?",
                    "Do you need a formal MoU or just informal support?"
                ],
                "examples": [
                    "Stakeholder: 'Block Education Officer (BEO) - Approves teacher training schedule.'"
                ]
            },
            "community": {
                "questions": [
                    "Who acts as the gatekeeper or leader in this community?",
                    "Are there marginalized groups within the community who currently aren't included?"
                ],
                "examples": [
                    "Stakeholder: 'Village Elders / Sarpanch - Influences community participation.'"
                ]
            },
            "parents": {
                "questions": [
                    "Are fathers and mothers equally involved?",
                    "What is their current attitude towards education?"
                ],
                "examples": [
                    "Stakeholder: 'School Management Committee (SMC) members.'"
                ]
            }
        }
    },
    
    "Activities": {
        "title": "Activities & Interventions",
        "defaults": {
            "questions": [
                "Is this activity directly linked to a specific root cause?",
                "Do you have the budget and expertise for this activity?",
                "Could this activity be sustained by the community later?"
            ],
            "examples": [
                "Activity: 'Conduct 3-day workshop on hygiene for 50 mothers.'",
                "Activity: 'Distribute 100 textbooks to the library.'"
            ]
        },
        "keywords": {
            "training": {
                "questions": [
                    "Is it a one-time event or continuous coaching?",
                    "How will you ensure they practice what they learned?"
                ],
                "examples": [
                    "Activity: 'Identify and train 5 local youth as Champions to provide ongoing support.'"
                ]
            },
            "app": {
                "questions": [
                    "Do the users have access to smartphones and data?",
                    "Who will provide technical support when it crashes?"
                ],
                "examples": [
                    "Activity: 'Pilot the app with 10 teachers first to gather feedback before full launch.'"
                ]
            },
            "meeting": {
                 "questions": [
                    "How will you encourage people to attend?",
                    "What is the clear agenda for the meeting?"
                ],
                "examples": [
                    "Activity: 'Host a quarterly town hall to present progress and gather feedback.'"
                ]
            }
        }
    },

    "Metrics": {
        "title": "Success Metrics",
        "defaults": {
            "questions": [
                "Is this metric 'SMART' (Specific, Measurable, Achievable, Relevant, Time-bound)?",
                "Is it easy to collect this data consistently?",
                "Does this measure effort (what you did) or impact (what changed)?"
            ],
            "examples": [
                "KPI: 'Percentage of students passing the end-of-year math exam.'",
                "Verification: 'School report cards and attendance registers.'"
            ]
        },
        "keywords": {
            "survey": {
                "questions": [
                    "Will the survey answers be biased? How can you get honest feedback?",
                    "Who will collect and analyze the survey data?"
                ],
                "examples": [
                    "Verification: 'Anonymous feedback forms dropped in a suggestion box.'"
                ]
            },
            "observation": {
                "questions": [
                    "Do you have a standard checklist for observations?",
                    "How often will observations happen?"
                ],
                "examples": [
                    "Verification: 'Monthly classroom observation rubric filled by the Headmaster.'"
                ]
            },
            "score": {
                "questions": [
                    "Does the test score reflect real learning?",
                    "Are you comparing against a baseline?"
                ],
                "examples": [
                    "KPI: '20% increase in average reading speed scores over 6 months.'"
                ]
            }
        }
    }
}
