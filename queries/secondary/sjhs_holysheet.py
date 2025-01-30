import gspread
import pandas as pd

from credentials.mongodb import students


def update_sjhs_data():

    query = {
        "School Name" : "San Juan High School"
    }

    cols = [
        # Demographics
        'Student Preferred Last Name',
        'Student Preferred First Name',
        'Grade Level',

        # Attendance
        'YTD Total Absences',
        'YTD Tardies',

        # TOSCRF
        'TOSCRF Grade Equivalent (BOY)',
        'TOSCRF Percentile Rank (BOY)',
        'TOSCRF Grade Equivalent (MOY)',
        'TOSCRF Percentile Rank (MOY)',

        # Wida
        'WIDA Comprehension',
        'WIDA Listening',
        'WIDA Literacy',
        'WIDA Oral',
        'WIDA Overall',
        'WIDA Reading',
        'WIDA Speaking',
        'WIDA Writing',
        
        # Aspire Plus
        '23-24 Composite Scale Score',
        '23-24 ELA Scale Score',
        '23-24 ELA Proficiency Level',
        '23-24 English Scale Score',
        '23-24 English Proficiency Level',
        '23-24 Reading Scale Score',
        '23-24 Reading Proficiency Level',
        '23-24 Math Scale Score',
        '23-24 Math Proficiency Level',
        '23-24 Science Scale Score',
        '23-24 Science Proficiency Level',
        '23-24 STEM Scale Score',
        '23-24 STEM Proficiency Level',

        # ACT
        'ACT Composite',
        'ACT English',
        'ACT Mathematics',
        'ACT Reading',
        'ACT STEM',
        'ACT Science Reasoning',
    ]

    df = pd.DataFrame(list(students.find(query)))

    df = df.loc[:, cols]
        
    # Authenticate with gspread
    gc = gspread.service_account('creds/service_account.json')

    # Open Google Sheet
    sjhs_worksheet = gc.open('SJHS Holysheet')
    sjhs_sheet = sjhs_worksheet.worksheet('data')

    return sjhs_sheet.update([df.columns.values.tolist()] + df.fillna('').values.tolist())

