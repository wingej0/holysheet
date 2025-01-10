from credentials.mongodb import cols_db


def attendance_cols():
    attendance = {
        "attendance" : [
            "Tardies",
            "Total Absences",
            "Total Excused Absences",
            "Total Unexcused Absences"
        ]
    }

    cols_db["attendance"].insert_one(attendance)
    