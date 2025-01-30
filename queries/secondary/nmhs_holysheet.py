import gspread
import pandas as pd

from credentials.mongodb import students


def update_nmhs_data():

    query = {
        "School Name" : "Navajo Mountain High School"
    }

    cols = [
        # Demographics
        'Student Preferred Last Name',
        'Student Preferred First Name',
        'Grade Level',

        # Attendance
        'Term 1 Total Absences',
        'Term 2 Total Absences',
        'Term 3 Total Absences',
        'YTD Total Absences',

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
        # 'ACT English\\Writing',
        'ACT Mathematics',
        'ACT Reading',
        'ACT STEM',
        'ACT Science Reasoning',
    ]

    df = pd.DataFrame(list(students.find(query)))

    df = df.loc[:, cols]
    df = df.fillna('').sort_values(by=['Grade Level', 'Student Preferred Last Name', 'Student Preferred First Name'])
    
    # Authenticate with gspread
    gc = gspread.service_account('creds/service_account.json')

    # Open Google Sheet
    nmhs_worksheet = gc.open('NMHS Holysheet')
    nmhs_sheet = nmhs_worksheet.worksheet('data')

    return nmhs_sheet.update([df.columns.values.tolist()] + df.fillna('').values.tolist())


