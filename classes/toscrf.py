from typing import Dict
import pandas as pd
from credentials.mongodb import students, cols_db


class Toscrf:
    def __init__(self, window: str, query: Dict[str, str]):
        self.window = window
        self.query = query
        self.cols = cols_db['toscrf']

    def get_cols(self):
        cols_dict = list(self.cols.find())
        toscrf_cols = cols_dict[0]['toscrf']
        db_cols = [f'TOSCRF {col} ({self.window})' for col in toscrf_cols]
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
