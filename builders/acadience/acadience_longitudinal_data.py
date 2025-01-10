import os
from datetime import datetime
import logging
import pandas as pd

from credentials.mongodb import students
from tools.parsers import remove_empty_string_values


def write_to_db(df, year):
    # Configure logging with timestamp format
    logging.basicConfig(filename='logs/acadience_log.txt', format='%(asctime)s %(message)s', level=logging.INFO)

    # Convert levels to numbers for spreadsheet ease
    string_to_numeric_dict = {
        'well below benchmark': 1,
        'below benchmark': 2,
        'at benchmark': 3,
        'above benchmark': 4,
    }

    df = df.replace(string_to_numeric_dict, regex=True)

    # Convert the dataframe to a list of dictionaries
    data_records = df.to_dict('records')

    for record in data_records:
        if not record["Student State ID"]:
            continue

        remove_empty_string_values(record)

        # Find the record in the database by SSID
        student_id = int(record["Student State ID"])  # Strip off the decimal 0
        matching_record = students.find_one({"SSID": str(student_id)})  # Convert to string

        # Append the benchmark period and year to the key before saving to database
        school_year = f"{year} "
        if matching_record:
            if record['Benchmark Period'] == "beginning":
                benchmark = " (BOY)"
            if record['Benchmark Period'] == "middle":
                benchmark = " (MOY)"
            if record['Benchmark Period'] == "end":
                benchmark = " (EOY)"

            # Delete the Student State ID and Benchmark Period fields
            del record['Student State ID']
            del record['Benchmark Period']
            updated_record = {school_year + key + benchmark: value for key, value in record.items()}

            # Update the found record with data from the dictionary
            result = students.update_one({"_id": matching_record["_id"]}, {"$set": updated_record})
            if result.modified_count > 0:
                logging.info(f"Record with _id: {matching_record['_id']} data updated at {datetime.now()}")
            elif result.matched_count == 0:
                logging.info(f"Inserted new record with _id: {matching_record['_id']} at {datetime.now()}")

def get_longitudinal_acadience_data():
    years = [
        '21-22',
        '22-23',
        '23-24'
    ]

    for year in years:
        csv_file = os.path.join(os.path.dirname(__file__), f'longitudinal_data/{year}.csv')
        df = pd.read_csv(csv_file)

        # Get only the data that we need
        # Define columns for reading and math
        reading_cols = [
            'Student State ID',
            'Benchmark Period',
            'FSF Score',
            'FSF Status',
            'LNF Score',
            'PSF Score',
            'PSF Status',
            'NWF CLS Score',
            'NWF CLS Status',
            'NWF WWR Score',
            'NWF WWR Status',
            'ORF WC Score',
            'ORF WC Status',
            'ORF Accuracy Score',
            'ORF Accuracy Status',
            'Retell Score',
            'Retell Status',
            'Retell Quality Score',
            'Retell Quality Status',
            'Maze Adjusted Score',
            'Maze Status',
            'Reading Composite Score',
            'Reading Composite Status',
            'Reading Composite Pathway',
            'Lexile Reading'
        ]

        math_cols = [
            'Student State ID',
            'Benchmark Period',
            'BQD Score',
            'BQD Status',
            'NIF Score',
            'NIF Status',
            'NNF Score',
            'NNF Status',
            'AQD Score',
            'AQD Status',
            'MNF Score',
            'MNF Status',
            'Comp Score',
            'Comp Status',
            'C&A Score',
            'C&A Status',
            'Math Composite Score',
            'Math Composite Status',
            'Math Composite Pathway'
        ]

        df = df.fillna('')
        # Split the dataframe into dictionaries with period as key and data as value
        split_df = {period: df[df['Benchmark Period'] == period] for period in df['Benchmark Period'].unique()}

        # Access individual DataFrames
        beginning_df = split_df.get('beginning', pd.DataFrame())
        middle_df = split_df.get('middle', pd.DataFrame())
        end_df = split_df.get('end', pd.DataFrame())

        acadience_dfs = {}

        # Create discreet dataframes for Reading and Math and save them in an dictionary
        if not beginning_df.empty:
            acadience_dfs['BOY Reading'] = beginning_df.loc[:, reading_cols]
            acadience_dfs['BOY Math'] = beginning_df.loc[:, math_cols]

        if not middle_df.empty:
            acadience_dfs['MOY Reading'] = middle_df.loc[:, reading_cols]
            acadience_dfs['MOY Math'] = middle_df.loc[:, math_cols]

        if not end_df.empty:
            acadience_dfs['EOY Reading'] = end_df.loc[:, reading_cols]
            acadience_dfs['EOY Math'] = end_df.loc[:, math_cols]

        for name in acadience_dfs:
            write_to_db(acadience_dfs[name], year)

