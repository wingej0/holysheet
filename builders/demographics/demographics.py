from datetime import datetime
import logging
import pandas as pd
import requests
from io import StringIO

from credentials.credentials import aspire_login, aspire_export
from credentials.mongodb import students
from tools.parsers import remove_empty_string_values


def get_demographic_data():
    # Configure logging with timestamp format
    logging.basicConfig(filename='/home/wingej0/dev/holysheet/logs/demographics_log.txt', format='%(asctime)s %(message)s', level=logging.INFO)

    # Open a requests session to login to Aspire
    session = requests.Session()

    # Open the login page and extract the session cookie
    r = session.post(aspire_login.url)
    cookie = r.cookies['ASP.NET_SessionId']

    # Add the cookie to the login headers
    aspire_login.headers["Cookie"] = f"ASP.NET_SessionId={cookie};"

    # Login
    login_response = session.request(
        "POST",
        aspire_login.url,
        data=aspire_login.payload,
        headers=aspire_login.headers
    )

    # Add the cookie to the export headers
    aspire_export.headers["Cookie"] = f"ASP.NET_SessionId={cookie};"

    # Make a request for the demographic data
    export_response = requests.request(
        "POST",
        aspire_export.url,
        data=aspire_export.payload,
        headers=aspire_export.headers
    )

    # Convert the response to a .csv for processing
    export_data = str(export_response.content, "utf-8")
    demographic_data: StringIO = StringIO(export_data)

    # Convert the .csv to a pandas dataframe
    aspire_df = pd.read_csv(demographic_data)

    # Define the columns that should be included in the dataframe
    aspire_cols = [
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

    aspire_df = aspire_df.loc[:, aspire_cols]

    # Remove the `.0` from the SSID and Student ID columns
    aspire_df['SSID'] = aspire_df['SSID'].astype(str).str.replace(r'\.0$', '', regex=True)
    aspire_df['Student ID'] = aspire_df['Student ID'].astype(str).str.replace(r'\.0$', '', regex=True)


    # Return the dataframe with the NaN values removed
    parsed_df = aspire_df.fillna('')

    data_records = parsed_df.to_dict('records')

    # Set Student ID as the ID field in the database
    for record in data_records:
        remove_empty_string_values(record)
        record["_id"] = record["Student ID"]
        # Remove trailing spaces from the school name
        record["School Name"] = record["School Name"].strip()
        result = students.update_one({"_id": record["_id"]}, {"$set": record}, upsert=True)
        if result.modified_count > 0:
            logging.info(f"Record with _id: {record['_id']} data updated at {datetime.now()}")
        elif result.matched_count == 0:
            logging.info(f"Inserted new record with _id: {record['_id']} at {datetime.now()}")

