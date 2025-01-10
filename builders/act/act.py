from datetime import datetime
import logging
import pandas as pd
import sqlalchemy as db

from credentials.aspire_db import server, database, username, password
from credentials.mongodb import students
from tools.parsers import remove_empty_string_values


def get_act_data():
    # Configure logging with timestamp format
    logging.basicConfig(filename='logs/act_log.txt', format='%(asctime)s %(message)s', level=logging.INFO)

    driver = "ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
    engine = db.create_engine(f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}")
    conn = engine.connect()

    sql_query = "select * from LEA.WingetAssessmentScores_View"

    df = pd.read_sql(sql_query, conn)

    act_df = df[df.ShortTitle == "ACT"]

    act_cols = [
        'StudentID',
        'Year',
        'Month',
        'Title',
        'Score',
    ]

    act_df = act_df.loc[:, act_cols]
    
    # Convert scores to numbers
    act_df['Score'] = pd.to_numeric(act_df['Score'].str.replace('-', '', regex=False), errors='coerce')
    act_df = act_df.dropna(subset=['Score'])
    
    df_sorted = act_df.sort_values(['StudentID', 'Year', 'Month', 'Title'], ascending=[True, False, False, False])
    
    # Group by StudentID and keep all rows with the most recent Year and Month
    df_most_recent = df_sorted.groupby('StudentID').apply(lambda x: x[(x['Year'] == x['Year'].max()) & (x['Month'] == x['Month'].max())])
    df_most_recent.reset_index(drop=True, inplace=True)
    act_df = df_most_recent.pivot(index='StudentID', columns='Title', values='Score').reset_index()

    act_df.fillna('', inplace=True)

    # Convert Student IDs to strings
    act_df.rename(columns={'StudentID': 'Student ID'}, inplace=True)
    act_df['Student ID'] = act_df['Student ID'].astype(str)

    data_records = act_df.to_dict('records')

    for record in data_records:
        remove_empty_string_values(record)
        student_id = record["Student ID"]
        matching_record = students.find_one({"Student ID": student_id})
        if matching_record:
            del record["Student ID"]
            # Append ACT to the keys
            updated_record = {"ACT " + key: value for key, value in record.items()}
            # Update the found record with data from the dictionary
            result = students.update_one({"_id": matching_record["_id"]}, {"$set": updated_record})
            if result.modified_count > 0:
                logging.info(f"Record with _id: {matching_record['_id']} data updated at {datetime.now()}")
            elif result.matched_count == 0:
                logging.info(f"Inserted new record with _id: {matching_record['_id']} at {datetime.now()}")

