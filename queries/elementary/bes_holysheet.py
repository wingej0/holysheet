import pandas as pd
import gspread

from classes.demographics import Demographics
from classes.acadience import Acadience
from classes.rise import Rise
from classes.wida import Wida
from classes.attendance import Attendance


def update_bes_data():
    query = {
        "School Name" : "Blanding Elementary School"
    }

    # Get demographics
    demographics = Demographics(query)
    demographics_df = demographics.get_students()
    demographics_cols = [
        'Student ID', 
        'Student Preferred Last Name', 
        'Student Preferred First Name', 
        'Grade Level', 
        'Student Ethnicity', 
        'Student Race', 
        'IEP Disability', 
        'Tribal Affiliation', 
        'ELL', 
    ]
    demographics_df = demographics_df.loc[:, demographics_cols]

    # Get Attendance
    attendance = Attendance(query, "24-25", False)
    attendance_df = attendance.get_students()

    # Get Wida
    wida = Wida(query)
    wida_df = wida.get_students()

    # Get Acadience Reading
    reading = Acadience("reading", query)
    reading_df = reading.get_students()
    reading_cols = [
        'Student ID', 

        # BOY (Ordered)
        'Reading Composite Score (BOY)', 
        'Reading Composite Status (BOY)', 
        'Reading Composite Score (BOY) Class Rank', 
        'Reading Composite Score (BOY) Quartile', 
        'LNF Score (BOY)', 
        'FSF Score (BOY)', 
        'FSF Status (BOY)',
        'PSF Score (BOY)', 
        'PSF Status (BOY)',
        'NWF CLS Score (BOY)', 
        'NWF CLS Status (BOY)',
        'NWF WWR Score (BOY)', 
        'NWF WWR Status (BOY)', 
        'ORF WC Score (BOY)',  
        'ORF WC Status (BOY)',
        'ORF Accuracy Score (BOY)', 
        'ORF Accuracy Status (BOY)',
        'Retell Score (BOY)', 
        'Retell Status (BOY)', 
        'Retell Quality Score (BOY)', 
        'Retell Quality Status (BOY)', 
        'Maze Adjusted Score (BOY)', 
        'Maze Status (BOY)', 
        'Lexile Reading (BOY)', 
    ]
    reading_df = reading_df.loc[:, reading_cols]

    # Get Acadience Math
    math = Acadience("math", query)
    math_df = math.get_students()
    math_cols = [
        'Student ID', 
        'Math Composite Score (BOY)', 
        'Math Composite Status (BOY)',
        'Math Composite Score (BOY) Class Rank', 
        'Math Composite Score (BOY) Quartile', 
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
        'Comp Score (BOY)', 
        'Comp Status (BOY)', 
        'C&A Score (BOY)', 
        'C&A Status (BOY)', 
    ]
    math_df = math_df.loc[:, math_cols]

    # Get Rise
    # ELA
    rise_ela = Rise("ela", query, "23-24")
    rise_ela_df = rise_ela.get_students()
    rise_ela_cols = [
        'Student ID', 
        '23-24 ELA Scale Score', 
        '23-24 ELA Performance',
        '23-24 ELA Scale Score Class Rank', 
        '23-24 ELA Scale Score Quartile',
        '23-24 Reading Informational Text Performance',
        '23-24 Reading Literature Performance',	
        '23-24 Listening Comprehension Performance',
        '23-24 Language Performance'
    ]
    rise_ela_df = rise_ela_df.loc[:, rise_ela_cols]

    # Math
    rise_math = Rise("math", query, "23-24")
    rise_math_df = rise_math.get_students()
    rise_math_cols = [
        'Student ID', 
        '23-24 Math Scale Score',
        '23-24 Math Performance',
        '23-24 Math Scale Score Class Rank', 
        '23-24 Math Scale Score Quartile',
        '23-24 Number and Operations - Fractions Performance',
        '23-24 Number and Operations in Base Ten Performance',
        '23-24 Geometry / The Number System Performance',
        '23-24 Functions Performance',
        '23-24 Statistics and Probability Performance',
        '23-24 Measurement and Data and Geometry Performance',
        '23-24 Operations and Algebraic Thinking Performance',
        '23-24 Expressions and Equations Performance'
    ]
    rise_math_df = rise_math_df.loc[:, rise_math_cols]

    # Science
    rise_science = Rise("science", query, "23-24", ["4th", "5th", "6th", "7th", "8th"])
    rise_science_df = rise_science.get_students()
    rise_science_cols = [
        'Student ID', 
        '23-24 Science Scale Score',
        '23-24 Science Performance', 
        '23-24 Science Scale Score Class Rank',
        '23-24 Science Scale Score Quartile',
        '23-24 Organisms Functioning in Their Environment Performance',
        '23-24 Energy Transfer Performance', '23-24 Wave Patterns Performance',
        '23-24 Observable Patterns in the Sky Performance'
    ]
    rise_science_df = rise_science_df.loc[:, rise_science_cols]

    dfs = [
        demographics_df,
        attendance_df,
        wida_df,
        reading_df,
        math_df,
        rise_ela_df,
        rise_math_df,
        rise_science_df
    ]

    # Merge dataframes iteratively
    merged_df = dfs[0] 
    for df in dfs[1:]:
        merged_df = pd.merge(merged_df, df, on='Student ID')

    # Authenticate with gspread
    gc = gspread.service_account('creds/service_account.json')

    # Open Google Sheet
    bes_worksheet = gc.open('BES Holysheet')
    bes_sheet = bes_worksheet.worksheet('data')

    return bes_sheet.update([merged_df.columns.values.tolist()] + merged_df.fillna('').values.tolist())
