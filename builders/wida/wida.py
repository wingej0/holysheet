from datetime import datetime
import logging
import pandas as pd
import sqlalchemy as db

from credentials.aspire_db import server, database, username, password
from credentials.mongodb import students
from tools.parsers import remove_empty_string_values


def get_wida_data():
    # Configure logging with timestamp format
    logging.basicConfig(filename='logs/wida_log.txt', format='%(asctime)s %(message)s', level=logging.INFO)

    driver = "ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
    engine = db.create_engine(f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}")
    conn = engine.connect()

    sql_query = "select * from LEA.WingetAssessmentScores_View"

    df = pd.read_sql(sql_query, conn)

    wida_df = df[(df.ShortTitle == "WIDA ACCESS") & (df.Year == 2023)]

    wida_cols = [
        'StudentID',
        'Title',
        'Score',
    ]

    wida_df = wida_df.loc[:, wida_cols]
    wida_df = wida_df[(wida_df.Score != '') & (wida_df.Score != 'NA')]
    wida_df = wida_df.apply(pd.to_numeric, errors='ignore')

    wida_df = wida_df.pivot_table(index='StudentID', columns='Title', values='Score').reset_index()
    wida_df.columns = wida_df.columns.str.replace('Proficiency Level -', 'WIDA')

    # Convert Student IDs to strings
    wida_df.rename(columns={'StudentID': 'Student ID'}, inplace=True)
    wida_df['Student ID'] = wida_df['Student ID'].astype(str)

    data_records = wida_df.to_dict('records')

    for record in data_records:
        remove_empty_string_values(record)
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

