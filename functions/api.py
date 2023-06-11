import requests
import json
import pandas as pd
from functions.config import *
from functions.api import *



def api_query(endpoint, params=None):
    response = requests.get(f"{base_url}{endpoint}", headers=headers, params=params)
    if response.status_code == 200:
        data = json.loads(response.text)
        print(f"API query successful for endpoint:{endpoint}", "\n")
        return data
    else:
        print(f"API query error for endpoint: {endpoint}, Statuscode:{response.status_code}", "\n")
        print(response.text)
        return None

def check_api_connection():
    endpoint = "ping"
    response = api_query(endpoint)

    if response is not None:
        print("Connection to API server successful!\n")
    else:
        print("Failed to connect to API server!\n")
        exit(1)

def get_filtered_samples(
        limit=None,
        offset=None,
        location1=None,
        location2=None,
        location3=None,
        setting=None,
        latitude=None,
        longitude=None,
        rocktype=None,
        rockclass=None,
        mineral=None,
        material=None,
        inclusiontype=None,
        sampletech=None,
        element=None,
        elementtype=None,
        value=None,
        title=None,
        publicationyear=None,
        doi=None,
        firstname=None,
        lastname=None,
        agemin=None,
        agemax=None,
        geoage=None,
        geoageprefix=None,
        lab=None
):
    endpoint = "queries/samples"

    filters = {
        key: value
        for key, value in locals().items()
        if key not in ["endpoint"] and value is not None
    }

    data = api_query(endpoint, params=filters)
    return data
