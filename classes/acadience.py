from typing import Dict
import pandas as pd
from credentials.mongodb import students, cols_db


class Acadience:
    def __init__(
            self, 
            assessment: str, 
            query: Dict[str, str], 
            year = "current", 
            grades = ["k", "1st", "2nd", "3rd", "4th", "5th", "6th"], 
            windows = ["BOY", "MOY", "EOY"]
        ):
        self.assessment = assessment
        self.query = query
        self.year = year
        self.grades = grades
        self.windows = windows
        self.cols = cols_db['acadience']

    def get_cols(self):
        cols_dict = list(self.cols.find())
        acadience_cols = list(set([c for cs in [col[self.assessment] for col in cols_dict if col['grade'] in self.grades] for c in cs]))
        db_cols = []
        for window in self.windows:
            if self.year == 'current':
                db_cols.extend([f'{col} ({window})' for col in acadience_cols])
                if self.assessment == 'math':
                    db_cols.append(f'Math Composite Score ({window}) Class Rank')
                    db_cols.append(f'Math Composite Score ({window}) Quartile')
                if self.assessment == 'reading':
                    db_cols.append(f'Reading Composite Score ({window}) Class Rank')
                    db_cols.append(f'Reading Composite Score ({window}) Quartile')
            else:
                db_cols.extend([f'{self.year} {col} ({window})' for col in acadience_cols])
                
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
    