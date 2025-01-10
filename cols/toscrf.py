from credentials.mongodb import cols_db


def toscrf_cols():
    toscrf = {
        "toscrf" : [
            "Form",
            "Test Date",
            "Raw Score",
            "Age",
            "Age Equivalent",
            "Grade Equivalent",
            "Percentile Rank",
            "Index Score",
            "Descriptive Term",
            "Lexile Score",
            "Class Rank",
            "Quartile"
        ]
    }

    cols_db["toscrf"].insert_one(toscrf)

