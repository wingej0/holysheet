from typing import Dict
import pandas as pd
from credentials.mongodb import students, cols_db


class AspirePlus:
    def __init__(
            self, 
            query: Dict[str, str], 
            year: str
        ):
        self.query = query
        self.year = year
        self.cols = cols_db['aspire_plus']
        self.current = "23-24"

    def get_cols(self):
        cols_dict = list(self.cols.find())
        aspire_plus_cols = cols_dict[0]['aspire_plus']
        db_cols = [f'{self.year} {col}' for col in aspire_plus_cols]
        if self.year == self.current:
            quartile_cols = [
                f"{self.year} Composite Scale Score Class Rank",
                f"{self.year} Composite Scale Score Quartile",
                f"{self.year} ELA Scale Score Class Rank",
                f"{self.year} ELA Scale Score Quartile",
                f"{self.year} English Scale Score Class Rank",
                f"{self.year} English Scale Score Quartile",
                f"{self.year} Reading Scale Score Class Rank",
                f"{self.year} Reading Scale Score Quartile",
                f"{self.year} Math Scale Score Class Rank",
                f"{self.year} Math Scale Score Quartile",
                f"{self.year} Science Scale Score Class Rank",
                f"{self.year} Science Scale Score Quartile",
                f"{self.year} STEM Scale Score Class Rank",
                f"{self.year} STEM Scale Score Quartile"
            ]
            db_cols.extend(quartile_cols)
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
    