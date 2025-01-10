import os
from datetime import datetime
import logging
import pandas as pd

from credentials.mongodb import students
from tools.parsers import remove_empty_string_values


def write_to_db(data_records, year):
    # Configure logging with timestamp format
    logging.basicConfig(filename='logs/rise_log.txt', format='%(asctime)s %(message)s', level=logging.INFO)

    for record in data_records:
        remove_empty_string_values(record)
        student_id = record["SSID"]
        matching_record = students.find_one({"SSID": student_id})
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


def get_rise_data():
    years = [
        # '20-21',
        '21-22',
        '22-23',
        '23-24',
    ]

    cols = [
        'Student ID',
        'ELA Scale Score',
        'ELA Performance',
        'Language Performance',
        'Listening Comprehension Performance',
        'Reading Informational Text Performance',
        'Reading Literature Performance',
        'Math Scale Score',
        'Math Performance',
        'Measurement and Data and Geometry Performance',
        'Number and Operations - Fractions Performance',
        'Number and Operations in Base Ten Performance',
        'Operations and Algebraic Thinking Performance',
        'Expressions and Equations Performance',
        'Geometry/Statistics and Probability Performance',
        'Ratios and Proportional Relationships Performance',
        'The Number System Performance',
        'Geometry Performance',
        'Statistics and Probability Performance',
        'Functions Performance',
        'Geometry / The Number System Performance',
        "Science Scale Score",
        "Science Performance",
        "Energy Transfer Performance",
        "Observable Patterns in the Sky Performance",
        "Organisms Functioning in Their Environment Performance",
        "Wave Patterns Performance",
        "Characteristics and Interactions of Earth's Systems Performance",
        "Cycling of Matter in Ecosystems Performance",
        "Properties and Changes of Matter Performance",
        "Earth's Weather Patterns and Climate Performance",
        "Energy Affects Matter Performance",
        "Stability and Change in Ecosystems Performance",
        "Structure and Motion within the Solar System Performance",
        "Changes in Species Over Time Performance",
        "Changes to Earth Over Time Performance",
        "Forces are Interactions Between Matter Performance",
        "Reproduction and Inheritance Performance",
        "Structure and Function of Life Performance",
        "Energy is Stored and Transferred in Physical Systems Performance",
        "Interactions with Natural Systems and Resources Performance",
        "Life Systems Store and Transfer Matter and Energy Performance",
        "Matter and Energy Interact in the Physical World Performance",
        'Writing Score',
        'Informative: Conventions of Standard English',
        'Informative: Evidence and Elaboration',
        'Informative: Purpose, Focus, and Organization',
        'Opinion: Conventions of Standard English',
        'Opinion: Evidence and Elaboration',
        'Opinion: Purpose, Focus, and Organization',
        'Argumentative: Conventions of Standard English',
        'Argumentative: Evidence and Elaboration',
        'Argumentative: Purpose, Focus, and Organization',
    ]

    sheets = [
        'ela3.csv',
        'ela4.csv',
        'ela5.csv',
        'ela6.csv',
        'ela7.csv',
        'ela8.csv',
        'math3.csv',
        'math4.csv',
        'math5.csv',
        'math6.csv',
        'math7.csv',
        'math8.csv',
        'science4.csv',
        'science5.csv',
        'science6.csv',
        'science7.csv',
        'science8.csv',
        'writing5.csv',
        'writing8.csv',
    ]

    titles = [
        'ELA Grade 3',
        'ELA Grade 4',
        'ELA Grade 5',
        'ELA Grade 6',
        'ELA Grade 7',
        'ELA Grade 8',
        'Math Grade 3',
        'Math Grade 4',
        'Math Grade 5',
        'Math Grade 6',
        'Math Grade 7',
        'Math Grade 8',
        'Science Grade 4',
        'Science Grade 5',
        'Science Grade 6',
        'Science Grade 7',
        'Science Grade 8',
        'Writing Grade 5',
        'Writing Grade 8',
    ]

    for year in years:
        for i in range(len(sheets)):
            csv_file = os.path.join(os.path.dirname(__file__), f'data/{year}/{sheets[i]}')
            df = pd.read_csv(csv_file)

            # Extract the subject from the titles string to rename the cols
            subject = titles[i].split(' ', 1)[0]

            # Rename the grade-specific columns
            df.rename(columns={f'Summative: {titles[i]} Scale Score': f'{subject} Scale Score'}, inplace=True)
            df.rename(columns={f'Summative: {titles[i]} Performance': f'{subject} Performance'}, inplace=True)

            # Get selected columns
            df_cols = list(df.keys())
            selected_cols = [col for col in df_cols if col in cols]
            df = df.loc[:, selected_cols]

            # Change the name of the 'Student ID' column in the Rise Data to 'SSID', so it matches the demographics data
            df.rename(columns={'Student ID': 'SSID'}, inplace=True)

            # Create a dictionary that maps the string values to the numeric values
            string_to_numeric_dict = {
                '1 - Below Proficient': 1,
                '2 - Approaching Proficient': 2,
                '3 - Proficient': 3,
                '4 - Highly Proficient': 4,
                'Insufficient to score': "",
                'Below Standard': 1,
                'At/Near Standard': 2,
                'Above Standard': 3,
            }

            df = df.replace(string_to_numeric_dict, regex=True)
            df = df.apply(pd.to_numeric, errors='ignore')

            # Convert SSID column to string
            df['SSID'] = df['SSID'].astype(str)

            data_records = df.to_dict('records')
            write_to_db(data_records, year)

