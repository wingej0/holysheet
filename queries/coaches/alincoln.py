import gspread
import pandas as pd

from credentials.mongodb import students


def update_amanda_data():
    
    query = {
        "School Name": {"$in" : ["Montezuma Creek Elementary", "Tse'bii'nidzisgai Elementary"]}
    }

    cols = [
        # Demographics
        'Student Preferred Last Name',
        'Student Preferred First Name',
        'Grade Level',
        'School Name',
        'Migrant',
        'Student Ethnicity',
        'Student Race',
        'Homeless',
        'IEP Disability',
        'ELL',

        # Attendance
        'YTD Total Absences',

        # WIDA
        'WIDA Comprehension',
        'WIDA Listening',
        'WIDA Literacy',
        'WIDA Oral',
        'WIDA Overall',
        'WIDA Reading',
        'WIDA Speaking',
        'WIDA Writing',

        # Acadience Reading (Current Year)
        'Reading Composite Score (BOY)',
        'Reading Composite Status (BOY)',
        'Lexile Reading (BOY)',
        'FSF Score (BOY)',
        'FSF Status (BOY)',
        'LNF Score (BOY)',
        'PSF Score (BOY)',
        'PSF Status (BOY)',
        'NWF CLS Score (BOY)',
        'NWF CLS Status (BOY)',
        'NWF WWR Score (BOY)',
        'NWF WWR Status (BOY)',
        'ORF Accuracy Score (BOY)',
        'ORF Accuracy Status (BOY)',
        'ORF WC Score (BOY)',
        'ORF WC Status (BOY)',
        'Retell Score (BOY)',
        'Retell Status (BOY)',
        'Retell Quality Score (BOY)',
        'Retell Quality Status (BOY)',
        'Maze Adjusted Score (BOY)',
        'Maze Status (BOY)',
        'Reading Composite Score (MOY)',
        'Reading Composite Status (MOY)',
        'Lexile Reading (MOY)',
        'FSF Score (MOY)',
        'FSF Status (MOY)',
        'LNF Score (MOY)',
        'PSF Score (MOY)',
        'PSF Status (MOY)',
        'NWF CLS Score (MOY)',
        'NWF CLS Status (MOY)',
        'NWF WWR Score (MOY)',
        'NWF WWR Status (MOY)',
        'ORF Accuracy Score (MOY)',
        'ORF Accuracy Status (MOY)',
        'ORF WC Score (MOY)',
        'ORF WC Status (MOY)',
        'Retell Score (MOY)',
        'Retell Status (MOY)',
        'Retell Quality Score (MOY)',
        'Retell Quality Status (MOY)',
        'Maze Adjusted Score (MOY)',
        'Maze Status (MOY)',

        # Acadience Math (Current Year)
        'Math Composite Score (BOY)',
        'Math Composite Status (BOY)',
        'BQD Score (BOY)',
        'BQD Status (BOY)',
        'NIF Score (BOY)',
        'NIF Status (BOY)',
        'NNF Score (BOY)',
        'NNF Status (BOY)',
        'AQD Score (BOY)',
        'AQD Status (BOY)',
        'MNF Score (BOY)',
        'MNF Status (BOY)',
        'C&A Score (BOY)',
        'C&A Status (BOY)',
        'Comp Score (BOY)',
        'Comp Status (BOY)',
        'Math Composite Score (MOY)',
        'Math Composite Status (MOY)',
        'BQD Score (MOY)',
        'BQD Status (MOY)',
        'NIF Score (MOY)',
        'NIF Status (MOY)',
        'NNF Score (MOY)',
        'NNF Status (MOY)',
        'AQD Score (MOY)',
        'AQD Status (MOY)',
        'MNF Score (MOY)',
        'MNF Status (MOY)',
        'C&A Score (MOY)',
        'C&A Status (MOY)',
        'Comp Score (MOY)',
        'Comp Status (MOY)',
    ]

    df = pd.DataFrame(list(students.find(query)))
    df = df.loc[:, cols]
    df.fillna('')

    # Authenticate with gspread
    gc = gspread.service_account('creds/service_account.json')

    # Open Google Sheet
    mzc_worksheet = gc.open('MZC Current Year')
    mzc_sheet = mzc_worksheet.worksheet('data')
    tes_worksheet = gc.open('TES Current Year')
    tes_sheet = tes_worksheet.worksheet('data')
    
    mzc = df[df['School Name'] == "Montezuma Creek Elementary"].drop(['School Name'], axis=1)
    tes = df[df['School Name'] == "Tse'bii'nidzisgai Elementary"].drop(['School Name'], axis=1)

    mzc_sheet.update([mzc.columns.values.tolist()] + mzc.fillna('').values.tolist())
    tes_sheet.update([tes.columns.values.tolist()] + tes.fillna('').values.tolist())
    return "Complete"

