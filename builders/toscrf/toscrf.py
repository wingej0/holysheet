from datetime import datetime
import logging
import gspread
import pandas as pd

from credentials.mongodb import students
from tools.parsers import remove_empty_string_values


def parse_toscrf_data(window):
    # Configure logging with timestamp format
    logging.basicConfig(filename='logs/toscrf_log.txt', format='%(asctime)s %(message)s', level=logging.INFO)

    # Authenticate with gspread
    gc = gspread.service_account('/home/wingej0/dev/holysheet/creds/service_account.json')
    toscrf_worksheet = gc.open('24-25 TOSCRF')
    toscrf_sheet = toscrf_worksheet.worksheet(window)

    # Convert Google Sheet to DataFrame
    toscrf_dict = toscrf_sheet.get_all_records()
    df = pd.DataFrame(toscrf_dict)

    # Convert strings to numbers and remove students without a test score
    df[['Raw Score', 'Index Score']] = df[['Raw Score', 'Index Score']].apply(pd.to_numeric)
    df = df[df['Descriptive Term'] != '']

    # Group by 'School Name' and 'Grade'
    grouped_df = df.groupby(['School Name', 'Grade'])

    # Calculate quartile ranks within each group
    df['Class Rank'] = grouped_df['Index Score'].rank(pct=True)

    # Define quartile boundaries
    quartiles = [0, 0.25, 0.5, 0.75, 1]

    # Assign quartile labels based on quartile ranks
    df['Quartile'] = pd.cut(df['Class Rank'], quartiles, labels=['Q4', 'Q3', 'Q2', 'Q1'])

    toscrf_cols = [
        'ID',
        'Form',
        'Test Date',
        'Raw Score',
        'Age',
        'Age Equivalent',
        'Grade Equivalent',
        'Percentile Rank',
        'Index Score',
        'Descriptive Term',
        'Lexile Score',
        'Class Rank',
        'Quartile'
    ]

    df = df.loc[:, toscrf_cols]

    # Convert Student IDs to strings
    df.rename(columns={'ID': 'Student ID'}, inplace=True)
    df['Student ID'] = df['Student ID'].astype(str)

    data_records = df.to_dict('records')
    
    for record in data_records:
        remove_empty_string_values(record)
        student_id = record["Student ID"]
        matching_record = students.find_one({"Student ID": student_id})
        if matching_record:
            del record["Student ID"]
            # Append TOSCRF to the keys
            updated_record = {f"TOSCRF {key} ({window})": value for key, value in record.items()}
            # Update the found record with data from the dictionary
            result = students.update_one({"_id": matching_record["_id"]}, {"$set": updated_record})
            if result.modified_count > 0:
                logging.info(f"Record with _id: {matching_record['_id']} data updated at {datetime.now()}")
            elif result.matched_count == 0:
                logging.info(f"Inserted new record with _id: {matching_record['_id']} at {datetime.now()}")


def get_toscrf_data():
    windows = ['BOY', 'MOY']
    for window in windows:
        parse_toscrf_data(window)

