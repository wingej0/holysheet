from credentials.mongodb import cols_db


def acadience_cols():
    acadience = [
        {
            'grade' : 'k', 
            'reading' : [
                'Reading Composite Score',
                'Reading Composite Status',
                'Reading Composite Pathway',
                'LNF Score',
                'FSF Score',
                'FSF Status',
                'PSF Score',
                'PSF Status',
                'NWF CLS Score',
                'NWF CLS Status',
                'NWF WWR Score',
                'NWF WWR Status',
                'Lexile Reading'
            ],
            'math' : [
                'Math Composite Score',
                'Math Composite Status',
                'Math Composite Pathway',
                'BQD Score',
                'BQD Status',
                'NIF Score',
                'NIF Status',
                'NNF Score',
                'NNF Status',
            ]
        },
        {
            'grade' : '1st',
            'reading' : [
                'Reading Composite Score',
                'Reading Composite Status',
                'Reading Composite Pathway',
                'PSF Score',
                'PSF Status',
                'NWF CLS Score',
                'NWF CLS Status',
                'NWF WWR Score',
                'NWF WWR Status',
                'ORF WC Score',
                'ORF WC Status',
                'ORF Accuracy Score',
                'ORF Accuracy Status',
                'Retell Score',
                'Retell Status',
                'Retell Quality Score',
                'Retell Quality Status',
                'Lexile Reading'
            ],
            'math' : [
                'Math Composite Score',
                'Math Composite Status',
                'Math Composite Pathway',
                'NIF Score',
                'NIF Status',
                'NNF Score',
                'NNF Status',
                'AQD Score',
                'AQD Status',
                'MNF Score',
                'MNF Status',
                'Comp Score',
                'Comp Status',
            ]
        },
        {
            'grade' : '2nd', 
            'reading' : [
                'Reading Composite Score',
                'Reading Composite Status',
                'Reading Composite Pathway',
                'NWF CLS Score',
                'NWF CLS Status',
                'NWF WWR Score',
                'NWF WWR Status',
                'ORF WC Score',
                'ORF WC Status',
                'ORF Accuracy Score',
                'ORF Accuracy Status',
                'Lexile Reading'
            ],
            'math' : [
                'Math Composite Score',
                'Math Composite Status',
                'Math Composite Pathway',
                'Comp Score',
                'Comp Status',
                'C&A Score',
                'C&A Status',
            ]
        },
        {
            'grade' : '3rd', 
            'reading' : [
                'Reading Composite Score',
                'Reading Composite Status',
                'Reading Composite Pathway',
                'ORF WC Score',
                'ORF WC Status',
                'ORF Accuracy Score',
                'ORF Accuracy Status',
                'Retell Score',
                'Retell Status',
                'Retell Quality Score',
                'Retell Quality Status',
                'Maze Adjusted Score',
                'Maze Status',
                'Lexile Reading'
            ],
            'math' : [
                'Math Composite Score',
                'Math Composite Status',
                'Math Composite Pathway',
                'Comp Score',
                'Comp Status',
                'C&A Score',
                'C&A Status',
            ]
        },
        {
            'grade' : '4th', 
            'reading' : [
                'Reading Composite Score',
                'Reading Composite Status',
                'Reading Composite Pathway',
                'ORF WC Score',
                'ORF WC Status',
                'ORF Accuracy Score',
                'ORF Accuracy Status',
                'Retell Score',
                'Retell Status',
                'Retell Quality Score',
                'Retell Quality Status',
                'Maze Adjusted Score',
                'Maze Status',
                'Lexile Reading'
            ],
            'math' : [
                'Math Composite Score',
                'Math Composite Status',
                'Math Composite Pathway',
                'Comp Score',
                'Comp Status',
                'C&A Score',
                'C&A Status',
            ]
        },
        {
            'grade' : '5th',
            'reading' : [
                'Reading Composite Score',
                'Reading Composite Status',
                'Reading Composite Pathway',
                'ORF WC Score',
                'ORF WC Status',
                'ORF Accuracy Score',
                'ORF Accuracy Status',
                'Retell Score',
                'Retell Status',
                'Retell Quality Score',
                'Retell Quality Status',
                'Maze Adjusted Score',
                'Maze Status',
                'Lexile Reading'
            ],
            'math' : [
                'Math Composite Score',
                'Math Composite Status',
                'Math Composite Pathway',
                'Comp Score',
                'Comp Status',
                'C&A Score',
                'C&A Status',
            ]
        },
        {
            'grade' : '6th', 
            'reading' : [
                'Reading Composite Score',
                'Reading Composite Status',
                'Reading Composite Pathway',
                'ORF WC Score',
                'ORF WC Status',
                'ORF Accuracy Score',
                'ORF Accuracy Status',
                'Retell Score',
                'Retell Status',
                'Retell Quality Score',
                'Retell Quality Status',
                'Maze Adjusted Score',
                'Maze Status',
                'Lexile Reading'
            ],
            'math' : [
                'Math Composite Score',
                'Math Composite Status',
                'Math Composite Pathway',
                'Comp Score',
                'Comp Status',
                'C&A Score',
                'C&A Status',
            ]
        },        
    ]

    cols_db["acadience"].insert_many(acadience)
