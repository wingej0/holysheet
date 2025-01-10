from typing import Dict
import pandas as pd
from credentials.mongodb import students, cols_db


class Attendance:
    def __init__(
            self, 
            query: Dict[str, str], 
            year: str, 
            terms: bool
        ):
        self.query = query
        self.year = year
        self.terms = terms
        self.cols = cols_db['attendance']
        self.current = "24-25"

    def get_cols(self):
        cols_dict = list(self.cols.find())
        attendance_cols = cols_dict[0]['attendance']
        terms_list = ["Term 1", "Term 2", "Term 3", "Term 4"]
        db_cols = [f"YTD {col}" for col in attendance_cols]
        if self.terms:
            for term in terms_list:
                term_cols = [f"{term} {col}" for col in attendance_cols]
                db_cols.extend(term_cols)
        if self.year != self.current:
            db_cols = [f"{self.year} {col}" for col in db_cols]
        db_cols.insert(0, 'Student ID')
        return db_cols
    
    def get_students(self):
        students_cols = self.get_cols()
        df = pd.DataFrame(list(students.find(self.query)))
        # Make sure all the keys are actually present in df
        check_keys = list(df.keys())
        valid_cols = [col for col in students_cols if col in check_keys]
        # Return the df with the selected cols
        df = df.loc[:, valid_cols]
        return df