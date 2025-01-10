import pandas as pd
from credentials.mongodb import students, cols_db


class Demographics:
    def __init__(self, query):
        self.cols = cols_db['demographics']
        self.query = query

    def get_cols(self):
        cols_dict = self.cols.find_one()
        return cols_dict['demographics']

    def get_students(self):
        cols = self.get_cols()
        df = pd.DataFrame(list(students.find(self.query)))
        # Make sure all the keys are actually present in df
        check_keys = list(df.keys())
        valid_cols = [col for col in cols if col in check_keys]
        # Return the df with the selected cols
        df = df.loc[:, valid_cols]
        return df
