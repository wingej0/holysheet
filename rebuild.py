from builders.acadience.acadience import get_acadience_data
from builders.acadience.acadience_longitudinal_data import get_longitudinal_acadience_data
from builders.act.act import get_act_data
from builders.aspire_plus.aspire_plus import get_aspire_plus_data
from builders.attendance.attendance import get_attendance_data
from builders.attendance.old_attendance import get_old_attendance_data
from builders.demographics.demographics import get_demographic_data
from builders.quartiles.quartiles import get_quartile_levels
from builders.rise.rise import get_rise_data
from builders.toscrf.toscrf import get_toscrf_data 
from builders.wida.wida import get_wida_data


def rebuild_database():

    # Get student demographic data first
    get_demographic_data()

    # Then get assessment data
    get_acadience_data()
    get_longitudinal_acadience_data()
    get_act_data()
    get_aspire_plus_data()
    get_rise_data()
    get_toscrf_data()
    get_wida_data()

    # Set quartile levels for each assessment
    get_quartile_levels()

    # Finally get attendance
    get_old_attendance_data()
    get_attendance_data()

    return "Database refreshed"


if __name__ == '__main__':
    rebuild_database()
