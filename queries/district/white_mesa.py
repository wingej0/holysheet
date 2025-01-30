import gspread
import pandas as pd

from credentials.mongodb import students


def update_white_mesa_data():

    query = {
        "Student Home City" : {"$in": ['White Mesa', 'White mesa']},
    }

    cols = [
        'Student Preferred First Name',
        'Student Preferred Last Name',
        'Grade Level',
        'Student Ethnicity',
        'Student Race',
        'Student Home City',
        'School Name',
        'Economically Disadvantaged',
        'IEP Disability',
        'Tribal Affiliation',
        'ELL',
        'Homeless',

        # Attendance
        'Term 1 Tardies',
        'Term 1 Total Absences',
        'Term 2 Tardies',
        'Term 2 Total Absences',
        'Term 3 Tardies',
        'Term 3 Total Absences',
        'YTD Tardies',
        'YTD Total Absences',

        # Wida
        'WIDA Overall',

        # Acadience
        '23-24 Reading Composite Score (EOY)',
        '23-24 Reading Composite Status (EOY)',
        '23-24 Math Composite Score (EOY)',
        '23-24 Math Composite Status (EOY)',
        'Reading Composite Score (BOY)',
        'Reading Composite Status (BOY)',
        'Math Composite Score (BOY)',
        'Math Composite Status (BOY)',
        'Reading Composite Score (MOY)',
        'Reading Composite Status (MOY)',
        'Math Composite Score (MOY)',
        'Math Composite Status (MOY)',

        # Aspire Plus
        '23-24 Composite Scale Score',
        '23-24 ELA Scale Score',
        '23-24 ELA Proficiency Level',
        '23-24 Math Scale Score',
        '23-24 Math Proficiency Level',
        '23-24 Science Scale Score',
        '23-24 Science Proficiency Level',

        # Rise
        '23-24 ELA Scale Score',
        '23-24 ELA Performance',
        '23-24 Math Scale Score',
        '23-24 Math Performance',
        '23-24 Science Scale Score',
        '23-24 Science Performance',

        # ACT
        'ACT Composite'
    ]

    df = pd.DataFrame(list(students.find(query)))

    df = df.loc[:, cols]
    df.fillna('')

    # Authenticate with gspread
    gc = gspread.service_account('creds/service_account.json')

    # Open Google Sheet
    wm_worksheet = gc.open('White Mesa')
    wm_sheet = wm_worksheet.worksheet('data')

    return wm_sheet.update([df.columns.values.tolist()] + df.fillna('').values.tolist())

