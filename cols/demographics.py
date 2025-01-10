from credentials.mongodb import cols_db


def demographics_cols():
    demographics = {
        "demographics" : [
            'Student ID',
            'SSID',
            'Student Preferred Last Name',
            'Student Preferred First Name',
            'Student Sex',
            'Student Birth Date',
            'Grade Level',
            'Student Ethnicity',
            'Student Race',
            'Student Home City',
            'School Name',
            'Economically Disadvantaged',
            'IEP Disability',
            'Tribal Affiliation',
            'YIC',
            'ELL',
            'Homeless',
            'Migrant',
            'Student Email Address',
            'Contact1 Last Name',
            'Contact1 First Name',
            'Contact1 Email Address',
        ]
    }

    cols_db["demographics"].insert_one(demographics)
    