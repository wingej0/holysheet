from credentials.mongodb import cols_db


def act_cols():
    act = {
        "act" : [
            "ACT Composite",
            "ACT English",
            "ACT Mathematics",
            "ACT Reading",
            "ACT STEM",
            "ACT Science Reasoning"
        ]
    }

    cols_db["act"].insert_one(act)