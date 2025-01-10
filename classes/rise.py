from typing import Dict
import pandas as pd
from credentials.mongodb import students, cols_db


class Rise:
    def __init__(
            self,
            assessment: str,
            query: Dict[str, str],
            year: str,
            grades = ["3rd", "4th", "5th", "6th", "7th", "8th"],
        ):
        self.assessment = assessment
        self.query = query
        self.year = year
        self.grades = grades
        self.cols = cols_db['rise']
        self.current = "23-24"

    def get_cols(self):
        cols_dict = list(self.cols.find())
        rise_cols = list(set([c for cs in [col[self.assessment] for col in cols_dict if col['grade'] in self.grades] for c in cs]))
        db_cols = [f'{self.year} {col}' for col in rise_cols]
        if self.year == self.current: 
            if self.assessment == 'ela':
                db_cols.append(f'{self.year} ELA Scale Score Class Rank')
                db_cols.append(f'{self.year} ELA Scale Score Quartile')
            if self.assessment == 'math':
                db_cols.append(f'{self.year} Math Scale Score Class Rank')
                db_cols.append(f'{self.year} Math Scale Score Quartile')
            if self.assessment == 'science':
                db_cols.append(f'{self.year} Science Scale Score Class Rank')
                db_cols.append(f'{self.year} Science Scale Score Quartile')
            if self.assessment == 'writing':
                db_cols.append(f'{self.year} Writing Scale Score Class Rank')
                db_cols.append(f'{self.year} Writing Scale Score Quartile')
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
    
    