import gspread

from classes.acadience import Acadience
from classes.act import Act
from classes.aspire_plus import AspirePlus
from classes.attendance import Attendance
from classes.demographics import Demographics
from classes.rise import Rise
from classes.toscrf import Toscrf
from classes.wida import Wida


def populate_sped_sheets():

    all_query = {
        "Grade Level" : { "$in" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] }
    }
    
    elementary_query = {
        "Grade Level" : { "$in" : [0, 1, 2, 3, 4, 5, 6] }
    }

    act_query = {
        "Grade Level" : { "$in" : [11, 12] }
    }

    aspire_plus_query = {
        "Grade Level" : { "$in" : [10, 11] }
    }

    rise_query = {
        "Grade Level" : { "$in" : [4, 5, 6, 7, 8, 9] }
    }

    toscrf_query = {
        "Grade Level" : { "$in" : [6, 7, 8, 9, 10, 11, 12] }
    }

    # Get dataframes
    acadience_reading = Acadience("reading", elementary_query)
    acadience_reading_df = acadience_reading.get_students()
    acadience_math = Acadience("math", elementary_query)
    acadience_math_df = acadience_math.get_students()
    act = Act(act_query)
    act_df = act.get_students()
    aspire_plus = AspirePlus(aspire_plus_query, "23-24")
    aspire_plus_df = aspire_plus.get_students()
    attendance = Attendance(all_query, "24-25", True)
    attendance_df = attendance.get_students()
    demographics = Demographics(all_query)
    demographics_df = demographics.get_students()
    rise_ela = Rise('ela', rise_query, "23-24")
    rise_ela_df = rise_ela.get_students()
    rise_math = Rise('math', rise_query, "23-24")
    rise_math_df = rise_math.get_students()
    rise_science = Rise('science', rise_query, "23-24", ["4th", "5th", "6th", "7th", "8th"])
    rise_science_df = rise_science.get_students()
    rise_writing = Rise('writing', rise_query, "23-24", ["5th", "8th"])
    rise_writing_df = rise_writing.get_students()
    toscrf_boy = Toscrf("BOY", toscrf_query)
    toscrf_boy_df = toscrf_boy.get_students()
    wida = Wida(all_query)
    wida_df = wida.get_students()
    
    # Authenticate with gspread
    gc = gspread.service_account('creds/service_account.json')
    worksheet = gc.open('24-25 Holysheet')

    dfs = {
        'Acadience Reading' : acadience_reading_df,
        'Acadience Math' : acadience_math_df,
        'ACT' : act_df,
        'Aspire Plus' : aspire_plus_df,
        'Attendance' : attendance_df,
        'Demographics' : demographics_df,
        'Rise ELA' : rise_ela_df,
        'Rise Math' : rise_math_df,
        'Rise Science' : rise_science_df,
        'Rise Writing' : rise_writing_df,
        'TOSCRF BOY' : toscrf_boy_df,
        'WIDA' : wida_df
    }

    for key, value in dfs.items():
        sheet = worksheet.worksheet(key)
        sheet.update([value.columns.values.tolist()] + value.fillna('').values.tolist())



if __name__ == '__main__':
    populate_sped_sheets()
    