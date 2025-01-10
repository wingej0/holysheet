from datetime import datetime
import logging
import pandas as pd
import sqlalchemy as db

from credentials.aspire_db import server, database, username, password
from credentials.mongodb import students


def get_attendance_data():
    driver = "ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
    engine = db.create_engine(f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}")
    conn = engine.connect()

    sql_query = "SELECT * FROM SJSD_CSS.dbo.AttendanceArchive WHERE SchoolYear = 2025"

    df = pd.read_sql(sql_query, conn)
    
    list_of_students = list(df.suniq.unique())

    attendance_data = []

    for student in list_of_students:
        student_df = df[df.suniq == student]
        school_id = list(student_df.trkuniq)
        student_attendance_data = {
            "Student ID": str(student),
            "School ID": str(school_id[0])
        }
        terms = student_df.termnum.unique()

        year_periods = student_df.shape[0]
        year_absences = student_df[student_df.inclass == 0].shape[0]
        year_unexcused = student_df[student_df.UnexcusedAbsenceFlag == 1].shape[0]
        year_excused = student_df[student_df.ExcusedAbsenceFlag == 1].shape[0]
        year_tardy = student_df[student_df.istardy == 1].shape[0]
        student_attendance_data['YTD Tardies'] = year_tardy
        student_attendance_data['YTD Total Absences'] = year_absences / year_periods
        student_attendance_data['YTD Total Excused Absences'] = year_excused / year_periods
        student_attendance_data['YTD Total Unexcused Absences'] = year_unexcused / year_periods
        
        for term in terms:
            student_df_by_term = student_df[student_df.termnum == term]
            total_periods = student_df_by_term.shape[0]
            total_absences = student_df_by_term[student_df_by_term.inclass == 0].shape[0]
            total_unexcused = student_df_by_term[student_df_by_term.UnexcusedAbsenceFlag == 1].shape[0]
            total_excused = student_df_by_term[student_df_by_term.ExcusedAbsenceFlag == 1].shape[0]
            total_tardy = student_df_by_term[student_df_by_term.istardy == 1].shape[0]
            student_attendance_data[f'Term {term} Tardies'] = total_tardy
            student_attendance_data[f'Term {term} Total Absences'] = total_absences / total_periods
            student_attendance_data[f'Term {term} Total Excused Absences'] = total_excused / total_periods
            student_attendance_data[f'Term {term} Total Unexcused Absences'] = total_unexcused / total_periods

        attendance_data.append(student_attendance_data)

    # Configure logging with timestamp format
    logging.basicConfig(filename='/home/wingej0/dev/holysheet/logs/attendance_log.txt', format='%(asctime)s %(message)s', level=logging.INFO)

    for record in attendance_data:
        matching_record = students.find_one({"Student ID": record["Student ID"]})
        if matching_record:
            result = students.update_one({"_id": matching_record["_id"]}, {"$set": record})

            if result.modified_count > 0:
                logging.info(f"Record with _id: {matching_record['_id']} data updated at {datetime.now()}")
            elif result.matched_count == 0:
                logging.info(f"Inserted new record with _id: {matching_record['_id']} at {datetime.now()}")

