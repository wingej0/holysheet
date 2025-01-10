from credentials.mongodb import cols_db


def wida_cols():
    wida = {
        "wida" : [
            "WIDA Overall",
            "WIDA Literacy",
            "WIDA Reading",
            "WIDA Writing",
            "WIDA Oral",
            "WIDA Speaking",
            "WIDA Listening",
            "WIDA Writing"
        ]
    }

    cols_db["wida"].insert_one(wida)
    