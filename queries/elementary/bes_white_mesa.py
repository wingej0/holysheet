import gspread
import pandas as pd

from credentials.mongodb import students


def update_bes_white_mesa_sheet():

    query = {
        "School Name" : "Blanding Elementary School",
        "Student Home City" : {"$in": ['White Mesa', 'White mesa']}
    }

    cols = [
        # Demographics
        'Student Preferred Last Name', 
        'Student Preferred First Name', 
        'Grade Level', 
        'Student Race',
        'Tribal Affiliation',
        'IEP Disability', 
        'ELL',

        # Attendance
        'Term 1 Total Absences',
        'Term 1 Tardies',
        'Term 2 Total Absences',
        'Term 2 Tardies',
        'Term 3 Total Absences',
        'Term 3 Tardies',

        # Wida
        'WIDA Overall',
        'WIDA Reading',
        'WIDA Comprehension',
        'WIDA Literacy',
        'WIDA Writing',
        'WIDA Oral',
        'WIDA Speaking',
        'WIDA Listening',

        # Acadience Reading
        'Reading Composite Score (BOY)',
        'Reading Composite Status (BOY)',
        'Lexile Reading (BOY)',
        'FSF Score (BOY)',
        'FSF Status (BOY)',
        'LNF Score (BOY)',
        'Maze Adjusted Score (BOY)',
        'Maze Status (BOY)',
        'NWF CLS Score (BOY)',
        'NWF CLS Status (BOY)',
        'NWF WWR Score (BOY)',
        'NWF WWR Status (BOY)',
        'ORF Accuracy Score (BOY)',
        'ORF Accuracy Status (BOY)',
        'ORF WC Score (BOY)',
        'ORF WC Status (BOY)',
        'Retell Quality Score (BOY)',
        'Retell Quality Status (BOY)',
        'Retell Score (BOY)',
        'Retell Status (BOY)',
        'Reading Composite Score (MOY)',
        'Reading Composite Status (MOY)',
        'Lexile Reading (MOY)',
        'FSF Score (MOY)',
        'FSF Status (MOY)',
        'LNF Score (MOY)',
        'Maze Adjusted Score (MOY)',
        'Maze Status (MOY)',
        'NWF CLS Score (MOY)',
        'NWF CLS Status (MOY)',
        'NWF WWR Score (MOY)',
        # 'NWF WWR Status (MOY)',
        'ORF Accuracy Score (MOY)',
        'ORF Accuracy Status (MOY)',
        'ORF WC Score (MOY)',
        'ORF WC Status (MOY)',
        'Retell Quality Score (MOY)',
        'Retell Quality Status (MOY)',
        'Retell Score (MOY)',
        'Retell Status (MOY)',

        # Acadience Math
        'Math Composite Score (BOY)',
        'Math Composite Status (BOY)',
        'BQD Score (BOY)',
        'BQD Status (BOY)',
        'C&A Score (BOY)',
        'C&A Status (BOY)',
        'Comp Score (BOY)',
        'Comp Status (BOY)',
        'NIF Score (BOY)',
        'NIF Status (BOY)',
        'NNF Score (BOY)',
        'NNF Status (BOY)',
        'Math Composite Score (MOY)',
        'Math Composite Status (MOY)',
        'BQD Score (MOY)',
        'BQD Status (MOY)',
        'C&A Score (MOY)',
        'C&A Status (MOY)',
        'Comp Score (MOY)',
        'Comp Status (MOY)',
        'NIF Score (MOY)',
        'NIF Status (MOY)',
        'NNF Score (MOY)',
        'NNF Status (MOY)',

        # Rise ELA
        '23-24 ELA Performance',
        '23-24 ELA Scale Score',
        '23-24 Language Performance',
        '23-24 Listening Comprehension Performance',
        '23-24 Reading Informational Text Performance',
        '23-24 Reading Literature Performance',

        # Rise Math
        '23-24 Math Performance',
        '23-24 Math Scale Score',
        '23-24 Measurement and Data and Geometry Performance',
        '23-24 Number and Operations - Fractions Performance',
        '23-24 Number and Operations in Base Ten Performance',
        '23-24 Operations and Algebraic Thinking Performance',

        # Rise Science
        '23-24 Science Performance',
        '23-24 Science Scale Score',
        '23-24 Energy Transfer Performance',
        '23-24 Observable Patterns in the Sky Performance',
        '23-24 Organisms Functioning in Their Environment Performance',
        '23-24 Wave Patterns Performance',
    ]

    df = pd.DataFrame(list(students.find(query)))
    df = df.loc[:, cols]

    df = df.fillna('').sort_values(by=['Grade Level', 'Student Preferred Last Name', 'Student Preferred First Name'])
    
    # Authenticate with gspread
    gc = gspread.service_account('creds/service_account.json')

    # Open Google Sheet
    bes_worksheet = gc.open('BES - White Mesa')
    bes_sheet = bes_worksheet.worksheet('Students')

    bes_sheet.update([df.columns.values.tolist()] + df.fillna('').values.tolist())

