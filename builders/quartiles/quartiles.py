from datetime import datetime
import logging
import pandas as pd

from credentials.mongodb import students
from tools.parsers import remove_nan_values


def get_quartile_levels():
    # Configure logging with timestamp format
    logging.basicConfig(filename='logs/quartiles_log.txt', format='%(asctime)s %(message)s', level=logging.INFO)

    query = {
    
    }

    cols = [
        'Student ID',
        'School Name',
        'Grade Level',
        'Reading Composite Score (BOY)',
        'Math Composite Score (BOY)',
        '23-24 ELA Scale Score',
        '23-24 Math Scale Score',
        '23-24 STEM Scale Score',
        '23-24 English Scale Score',
        '23-24 Reading Scale Score',
        '23-24 Science Scale Score',
        '23-24 Composite Scale Score',
    ]

    df = pd.DataFrame(list(students.find(query)))
    df = df.loc[:, cols]

    assessment_cols = cols[3:]

    grouped_df = df.groupby(['School Name', 'Grade Level'])

    for assessment in assessment_cols:
        df[f'{assessment} Class Rank'] = grouped_df[assessment].rank(pct=True)

        # Define quartile boundaries
        quartiles = [0, 0.25, 0.5, 0.75, 1]

        # Assign quartile labels based on quartile ranks
        df[f'{assessment} Quartile'] = pd.cut(df[f'{assessment} Class Rank'], quartiles, labels=['Q4', 'Q3', 'Q2', 'Q1'])

    # Filter out the queried columns, leaving only the new ones
    new_cols = [col for col in list(df.keys()) if col.endswith(('ID', 'Rank', 'Quartile'))]
    df = df.loc[:, new_cols]

    # Convert Student IDs to strings
    df.rename(columns={'ID': 'Student ID'}, inplace=True)
    df['Student ID'] = df['Student ID'].astype(str)

    data_records = df.to_dict('records')
    
    for record in data_records:
        remove_nan_values(record)
        student_id = record["Student ID"]
        matching_record = students.find_one({"Student ID": student_id})
        if matching_record:
            del record["Student ID"]
            # Update the found record with data from the dictionary
            result = students.update_one({"_id": matching_record["_id"]}, {"$set": record})
            if result.modified_count > 0:
                logging.info(f"Record with _id: {matching_record['_id']} data updated at {datetime.now()}")
            elif result.matched_count == 0:
                logging.info(f"Inserted new record with _id: {matching_record['_id']} at {datetime.now()}")

