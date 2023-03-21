import json
import datetime as dt
import pandas
import numpy as np
import requests
from dmi_open_data import DMIOpenDataClient, Parameter, ClimateDataParameter


def RetrieveJSON():

    client = DMIOpenDataClient(api_key = '38e8862d-e5dc-4b25-9eba-d18d491d815b')
    stations = client.get_stations(limit=10)

    parameters = client.list_parameters()

    import requests

    api_key = '38e8862d-e5dc-4b25-9eba-d18d491d815b' # replace with your actual API key
    url = f'https://dmigw.govcloud.dk/v2/metObs/collections/observation/items?api-key={api_key}'

    headers = {'Authorization': f'Bearer {api_key}'}
    params = {'stationId': '06187', 'limit': 10}  # replace with your desired parameters

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        # do something with the data
    else:
        print(f'Request failed with status code {response.status_code}')

RetrieveJSON()