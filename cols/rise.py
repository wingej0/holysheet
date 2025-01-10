from credentials.mongodb import cols_db


def rise_cols():
    rise_cols = [
        {
            "grade" : "3rd",
            "ela" : [
                'ELA Scale Score',
                'ELA Performance',
                'Language Performance',
                'Listening Comprehension Performance',
                'Reading Informational Text Performance',
                'Reading Literature Performance',
            ],
            "math" : [
                'Math Scale Score',
                'Math Performance',
                'Measurement and Data and Geometry Performance',
                'Number and Operations - Fractions Performance',
                'Number and Operations in Base Ten Performance',
                'Operations and Algebraic Thinking Performance',
            ]
        },
        {
            "grade" : "4th",
            "ela" : [
                'ELA Scale Score',
                'ELA Performance',
                'Language Performance',
                'Listening Comprehension Performance',
                'Reading Informational Text Performance',
                'Reading Literature Performance',
            ],
            "math" : [
                'Math Scale Score',
                'Math Performance',
                'Measurement and Data and Geometry Performance',
                'Number and Operations - Fractions Performance',
                'Number and Operations in Base Ten Performance',
                'Operations and Algebraic Thinking Performance',
            ],
            "science" : [
                "Science Scale Score",
                "Science Performance",
                "Energy Transfer Performance",
                "Observable Patterns in the Sky Performance",
                "Organisms Functioning in Their Environment Performance",
                "Wave Patterns Performance",
            ]
        },
        {
            "grade" : "5th",
            "ela" : [
                'ELA Scale Score',
                'ELA Performance',
                'Language Performance',
                'Listening Comprehension Performance',
                'Reading Informational Text Performance',
                'Reading Literature Performance',
            ],
            "math" : [
                'Math Scale Score',
                'Math Performance',
                'Measurement and Data and Geometry Performance',
                'Number and Operations - Fractions Performance',
                'Number and Operations in Base Ten Performance',
                'Operations and Algebraic Thinking Performance',
            ],
            "science" : [
                "Science Scale Score",
                "Science Performance",
                "Characteristics and Interactions of Earth's Systems Performance",
                "Cycling of Matter in Ecosystems Performance",
                "Properties and Changes of Matter Performance",
            ],
            "writing" : [
                "Writing Score",
                "Informative: Conventions of Standard English",
                "Informative: Evidence and Elaboration",
                "Informative: Purpose, Focus, and Organization",
                "Opinion: Conventions of Standard English",
                "Opinion: Evidence and Elaboration",
                "Opinion: Purpose, Focus, and Organization",
            ]
        },
        {
            "grade" : "6th",
            "ela" : [
                'ELA Scale Score',
                'ELA Performance',
                'Language Performance',
                'Listening Comprehension Performance',
                'Reading Informational Text Performance',
                'Reading Literature Performance',
            ],
            "math" : [
                'Math Scale Score',
                'Math Performance',
                'Expressions and Equations Performance',
                'Geometry/Statistics and Probability Performance',
                'Ratios and Proportional Relationships Performance',
                'The Number System Performance',
            ],
            "science" : [
                "Science Scale Score",
                "Science Performance",
                "Earth's Weather Patterns and Climate Performance",
                "Energy Affects Matter Performance",
                "Stability and Change in Ecosystems Performance",
                "Structure and Motion within the Solar System Performance",
            ]
        },
        {
            "grade" : "7th",
            "ela" : [
                'ELA Scale Score',
                'ELA Performance',
                'Language Performance',
                'Listening Comprehension Performance',
                'Reading Informational Text Performance',
                'Reading Literature Performance',
            ],
            "math" : [
                'Math Scale Score',
                'Math Performance',
                'Expressions and Equations Performance',
                'Geometry Performance',
                'Ratios and Proportional Relationships Performance',
                'Statistics and Probability Performance',
                'The Number System Performance',
            ],
            "science" : [
                "Science Scale Score",
                "Science Performance",
                "Changes in Species Over Time Performance",
                "Changes to Earth Over Time Performance",
                "Forces are Interactions Between Matter Performance",
                "Reproduction and Inheritance Performance",
                "Structure and Function of Life Performance",
            ]
        },
        {
            "grade" : "8th",
            "ela" : [
                'ELA Scale Score',
                'ELA Performance',
                'Language Performance',
                'Listening Comprehension Performance',
                'Reading Informational Text Performance',
                'Reading Literature Performance',
            ],
            "math" : [
                'Math Scale Score',
                'Math Performance',
                'Expressions and Equations Performance',
                'Functions Performance',
                'Geometry / The Number System Performance',
                'Statistics and Probability Performance',
            ],
            "science" : [
                "Science Scale Score",
                "Science Performance",
                "Energy is Stored and Transferred in Physical Systems Performance",
                "Interactions with Natural Systems and Resources Performance",
                "Life Systems Store and Transfer Matter and Energy Performance",
                "Matter and Energy Interact in the Physical World Performance",
            ],
            "writing" : [
                "Writing Score",
                "Argumentative: Conventions of Standard English",
                "Argumentative: Evidence and Elaboration",
                "Argumentative: Purpose, Focus, and Organization",
                "Informative: Conventions of Standard English",
                "Informative: Evidence and Elaboration",
                "Informative: Purpose, Focus, and Organization",
            ]
        },
    ]

    cols_db["rise"].insert_many(rise_cols)
    