# Coaches
from queries.coaches.alincoln import update_amanda_data

# District
from queries.district.white_mesa import update_white_mesa_data

# Elementary
from queries.elementary.bes_holysheet import update_bes_data
from queries.elementary.bes_white_mesa import update_bes_white_mesa_sheet
from queries.elementary.mzc_holysheet import update_mzc_data

# Secondary
from queries.secondary.arl_holysheet import update_arl_holysheet
from queries.secondary.mhs_holysheet import update_mhs_data
from queries.secondary.mvhs_holysheet import update_mvhs_data
from queries.secondary.nmhs_holysheet import update_nmhs_data
from queries.secondary.sjhs_holysheet import update_sjhs_data


def update_data_sheets():
    # Coaches
    update_amanda_data()

    # District
    update_white_mesa_data()

    # Elementary
    update_bes_data()
    update_bes_white_mesa_sheet()
    update_mzc_data()

    # Secondary
    update_arl_holysheet()
    update_mhs_data()
    update_mvhs_data()
    update_nmhs_data()
    update_sjhs_data()

    return


if __name__ == '__main__':
    update_data_sheets()
    