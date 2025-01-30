import gspread
import pandas as pd

from credentials.mongodb import students


def update_arl_holysheet():

    query = {
        "School Name" : "Albert R. Lyman Middle School"
    }

    cols = [
        # Demographics
        'Student Preferred Last Name', 
        'Student Preferred First Name', 
        'Grade Level', 
        'Student Race', 
        'IEP Disability', 
        'ELL',

        # Attendance
        'Term 1 Total Absences', 
        'Term 2 Total Absences',
        'Term 3 Total Absences',

        # Wida
        'WIDA Overall',
        'WIDA Reading',
        'WIDA Comprehension',
        'WIDA Literacy',
        'WIDA Writing',
        'WIDA Oral',
        'WIDA Speaking',
        'WIDA Listening',
        
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
        '23-24 Expressions and Equations Performance',
        '23-24 Geometry Performance',
        '23-24 Geometry/Statistics and Probability Performance',
        '23-24 Measurement and Data and Geometry Performance',
        '23-24 Number and Operations - Fractions Performance',
        '23-24 Number and Operations in Base Ten Performance',
        '23-24 Operations and Algebraic Thinking Performance',
        '23-24 Ratios and Proportional Relationships Performance',
        '23-24 Statistics and Probability Performance',
        '23-24 The Number System Performance',

        # Rise Science
        '23-24 Science Performance',
        '23-24 Science Scale Score',
        '23-24 Changes in Species Over Time Performance',
        '23-24 Changes to Earth Over Time Performance',
        "23-24 Characteristics and Interactions of Earth's Systems Performance",
        '23-24 Cycling of Matter in Ecosystems Performance',
        "23-24 Earth's Weather Patterns and Climate Performance",
        '23-24 Energy Affects Matter Performance',
        '23-24 Forces are Interactions Between Matter Performance',
        '23-24 Properties and Changes of Matter Performance',
        '23-24 Reproduction and Inheritance Performance',
        '23-24 Stability and Change in Ecosystems Performance',
        '23-24 Structure and Function of Life Performance',
        '23-24 Structure and Motion within the Solar System Performance',

        # TOSCRF
        'TOSCRF Grade Equivalent (BOY)',
        'TOSCRF Percentile Rank (BOY)',
        'TOSCRF Descriptive Term (BOY)',
        'TOSCRF Grade Equivalent (MOY)',
        'TOSCRF Percentile Rank (MOY)',
        'TOSCRF Descriptive Term (MOY)',
    ]

    df = pd.DataFrame(list(students.find(query)))

    df = df.loc[:, cols]
    df = df.fillna('').sort_values(by=['Student Preferred Last Name', 'Student Preferred First Name'])

    race_abbreviations = {
        'American Indian or Alaska Native': 'AI',
        'Black or African American': 'B',
        'Multiple': 'M',
        'White': 'W'
    }

    df = df.replace(race_abbreviations, regex=True)
    
    # Authenticate with gspread
    gc = gspread.service_account('creds/service_account.json')

    # Open Google Sheet
    arl_worksheet = gc.open('ARL Holysheet')
    arl_sheet = arl_worksheet.worksheet('arl-hs')

    arl_sheet.update([df.columns.values.tolist()] + df.fillna('').values.tolist())

