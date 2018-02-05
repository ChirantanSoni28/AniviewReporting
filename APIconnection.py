import requests as req
import json
import ijson
import numpy as np
import pandas as pd
from AniviewReporting.URLgenerator import urlgen

def connector():
    payload = {
    "id" : "chirantan@thrive.plus",
    "password" : "changeme"
    }
    response = req.post('http://manage.aniview.com/api/token?format=json', json = payload)


    # print(response.status_code)
    # print(response.text)
    token = response.json()
    # print(token['data'])
    url = urlgen()
    labels = ['Pub_id', 'Pub_Name', 'Pub_channel_Name', 'Channel_Name', 'Inventory', 'Requests', 'Impressions',
               'Revenue', 'Cost', 'Profit']
    response2 = req.get(url, cookies=token['data'])
    print(response2.status_code)
    data_json = response2.json()

    df = pd.DataFrame.from_dict(data_json['data'])
    cols = df.columns.tolist()
    order = [3,4,6,7,2,8,1,9,0,5]
    cols = [cols[i] for i in order]
    # print(cols)
    df = df[cols]
    df.columns = labels
    # print(df['Network/publisher Name'])
    # print(df.shape)
    # data = data_json['data'][0]
    # print(data)
    return df
# print(connector())
