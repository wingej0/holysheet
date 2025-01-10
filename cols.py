from cols.acadience import acadience_cols
from cols.act import act_cols
from cols.aspire_plus import aspire_plus_cols
from cols.attendance import attendance_cols
from cols.demographics import demographics_cols
from cols.rise import rise_cols
from cols.toscrf import toscrf_cols
from cols.wida import wida_cols


def rebuild_cols_db():
    acadience_cols()
    act_cols()
    aspire_plus_cols()
    attendance_cols()
    demographics_cols()
    rise_cols()
    toscrf_cols()
    wida_cols()

    return "Cols DB Refreshed"


if __name__ == '__main__':
    rebuild_cols_db()
