from credentials.mongodb import cols_db


def acadience_cols():
    acadience = [
        {
            'grade' : 'k', 
            'reading' : [
                'LNF Score',
                'FSF Score',
                'FSF Status',
                'PSF Score',
                'PSF Status',
                'NWF CLS Score',
                'NWF CLS Status',
                'NWF WWR Score',
                'NWF WWR Status',
                'Reading Composite Score',
                'Reading Composite Status',
                'Reading Composite Pathway',
                'Lexile Reading'
            ],
            'math' : [
                'BQD Score',
                'BQD Status',
                'NIF Score',
                'NIF Status',
                'NNF Score',
                'NNF Status',
                'Math Composite Score',
                'Math Composite Status',
                'Math Composite Pathway'
            ]
        },
        {
            'grade' : '1st',
            'reading' : [
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
                'Reading Composite Score',
                'Reading Composite Status',
                'Reading Composite Pathway',
                'Lexile Reading'
            ],
            'math' : [
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
                'Math Composite Score',
                'Math Composite Status',
                'Math Composite Pathway'
            ]
        },
        {
            'grade' : '2nd', 
            'reading' : [
                'NWF CLS Score',
                'NWF CLS Status',
                'NWF WWR Score',
                'NWF WWR Status',
                'ORF WC Score',
                'ORF WC Status',
                'ORF Accuracy Score',
                'ORF Accuracy Status',
                'Reading Composite Score',
                'Reading Composite Status',
                'Reading Composite Pathway',
                'Lexile Reading'
            ],
            'math' : [
                'Comp Score',
                'Comp Status',
                'C&A Score',
                'C&A Status',
                'Math Composite Score',
                'Math Composite Status',
                'Math Composite Pathway'
            ]
        },
        {
            'grade' : '3rd', 
            'reading' : [
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
                'Reading Composite Score',
                'Reading Composite Status',
                'Reading Composite Pathway',
                'Lexile Reading'
            ],
            'math' : [
                'Comp Score',
                'Comp Status',
                'C&A Score',
                'C&A Status',
                'Math Composite Score',
                'Math Composite Status',
                'Math Composite Pathway'
            ]
        },
        {
            'grade' : '4th', 
            'reading' : [
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
                'Reading Composite Score',
                'Reading Composite Status',
                'Reading Composite Pathway',
                'Lexile Reading'
            ],
            'math' : [
                'Comp Score',
                'Comp Status',
                'C&A Score',
                'C&A Status',
                'Math Composite Score',
                'Math Composite Status',
                'Math Composite Pathway'
            ]
        },
        {
            'grade' : '5th',
            'reading' : [
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
                'Reading Composite Score',
                'Reading Composite Status',
                'Reading Composite Pathway',
                'Lexile Reading'
            ],
            'math' : [
                'Comp Score',
                'Comp Status',
                'C&A Score',
                'C&A Status',
                'Math Composite Score',
                'Math Composite Status',
                'Math Composite Pathway'
            ]
        },
        {
            'grade' : '6th', 
            'reading' : [
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
                'Reading Composite Score',
                'Reading Composite Status',
                'Reading Composite Pathway',
                'Lexile Reading'
            ],
            'math' : [
                'Comp Score',
                'Comp Status',
                'C&A Score',
                'C&A Status',
                'Math Composite Score',
                'Math Composite Status',
                'Math Composite Pathway'
            ]
        },        
    ]

    cols_db["acadience"].insert_many(acadience)
