import os
from datetime import datetime
import logging
import re
import pandas as pd

from credentials.mongodb import students
from tools.parsers import remove_empty_string_values


def write_to_db(data_records, year):
    # Configure logging with timestamp format
    logging.basicConfig(filename='logs/aspire_plus_log.txt', format='%(asctime)s %(message)s', level=logging.INFO)

    for record in data_records:
        remove_empty_string_values(record)
        student_id = record["SSID"]
        matching_record = students.find_one({"Student ID": student_id})
        if matching_record:
            del record["SSID"]
            # Add years to the keys
            updated_record = {year + " " + key: value for key, value in record.items()}

            # Update the found record with data from the dictionary
            result = students.update_one({"_id": matching_record["_id"]}, {"$set": updated_record})
            if result.modified_count > 0:
                logging.info(f"Record with _id: {matching_record['_id']} data updated at {datetime.now()}")
            elif result.matched_count == 0:
                logging.info(f"Inserted new record with _id: {matching_record['_id']} at {datetime.now()}")


def get_aspire_plus_data():
    years = [
        # "18-19",
        "20-21",
        "21-22",
        "22-23",
        "23-24"
    ]

    for year in years:
        csv_file = os.path.join(os.path.dirname(__file__), f'data/{year}.csv')
        df = pd.read_csv(csv_file)

        cols = [
            'LocalStudentID',
            'CompositeScaleScore',
            'CompositePredictedACTScore',
            'CompositePredictedACTScoreRangeLow',
            'CompositePredictedACTScoreRangeHigh',
            'ELAScaleScore',
            'ELAProficiencyLevel',
            'STEMScaleScore',
            'STEMProficiencyLevel',
            'EnglishScaleScore',
            'EnglishProficiencyLevel',
            'EnglishPredictedACTScore',
            'EnglishPredictedACTScoreRangeLow',
            'EnglishPredictedACTScoreRangeHigh',
            'ReadingScaleScore',
            'ReadingProficiencyLevel',
            'ReadingPredictedACTScore',
            'ReadingPredictedACTScoreRangeLow',
            'ReadingPredictedACTScoreRangeHigh',
            'MathScaleScore',
            'MathProficiencyLevel',
            'MathPredictedACTScore',
            'MathPredictedACTScoreRangeLow',
            'MathPredictedACTScoreRangeHigh',
            'ScienceScaleScore',
            'ScienceProficiencyLevel',
            'SciencePredictedACTScore',
            'SciencePredictedACTScoreRangeLow',
            'SciencePredictedACTScoreRangeHigh',
        ]

        df = df.loc[:, cols]

        # Reformat camel case column titles
        df = df.rename(columns=lambda x: re.sub(r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))', r'\1 ', x)).copy()
        
        # Rename SSID column to match database
        df.rename(columns={'Local Student ID': 'SSID'}, inplace=True)

        # Convert SSID column to string
        df['SSID'] = df['SSID'].astype(str)

        data_records = df.to_dict('records')
        write_to_db(data_records, year)

    
