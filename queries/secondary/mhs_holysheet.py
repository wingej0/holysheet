import gspread
import pandas as pd

from credentials.mongodb import students


def update_mhs_data():

    query = {
        "School Name" : "Monticello High School"
    }

    cols = [
        # Demographics
        'Student Preferred Last Name',
        'Student Preferred First Name',
        'Grade Level',
        'Economically Disadvantaged',
        'IEP Disability',
        'ELL',

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

        # Rise
        '23-24 ELA Scale Score',
        '23-24 ELA Performance', 
        '23-24 Listening Comprehension Performance', 
        '23-24 Reading Informational Text Performance', 
        '23-24 Reading Literature Performance', 
        '23-24 Language Performance', 
        '23-24 Math Scale Score', 
        '23-24 Math Performance',
        '23-24 Expressions and Equations Performance', 
        '23-24 The Number System Performance', 
        '23-24 Ratios and Proportional Relationships Performance', 
        '23-24 Geometry / The Number System Performance', 
        '23-24 Geometry/Statistics and Probability Performance', 
        '23-24 Statistics and Probability Performance',  
        '23-24 Geometry Performance', 
        '23-24 Functions Performance',
        '23-24 Science Scale Score', 
        '23-24 Science Performance', 
        '23-24 Changes to Earth Over Time Performance', 
        '23-24 Energy is Stored and Transferred in Physical Systems Performance', 
        '23-24 Interactions with Natural Systems and Resources Performance', 
        '23-24 Energy Affects Matter Performance', 
        '23-24 Structure and Motion within the Solar System Performance', 
        '23-24 Changes in Species Over Time Performance', 
        '23-24 Reproduction and Inheritance Performance', 
        '23-24 Forces are Interactions Between Matter Performance', 
        '23-24 Life Systems Store and Transfer Matter and Energy Performance', 
        "23-24 Earth's Weather Patterns and Climate Performance", 
        '23-24 Structure and Function of Life Performance', 
        '23-24 Stability and Change in Ecosystems Performance', 
        '23-24 Matter and Energy Interact in the Physical World Performance', 
        '23-24 Argumentative: Purpose, Focus, and Organization', 
        '23-24 Informative: Conventions of Standard English', 
        '23-24 Informative: Purpose, Focus, and Organization', 
        '23-24 Argumentative: Evidence and Elaboration', 
        '23-24 Argumentative: Conventions of Standard English', 
        '23-24 Informative: Evidence and Elaboration',
        
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
    mhs_worksheet = gc.open('MHS Holysheet')
    mhs_sheet = mhs_worksheet.worksheet('data')

    return mhs_sheet.update([df.columns.values.tolist()] + df.fillna('').values.tolist())

