import requests as req
import json
import ijson
import numpy as np
import pandas as pd
from AniviewReporting.URLgenerator import urlgen

"""The Below function sorts the column of a dataframe as required in the reports"""



def alterColumns_pub(df):
    orderedList = ['Date','Pub_id', 'Pub_Name', 'Pub_Channel_id', 'Pub_channel_Name', 'Channel_Name', 'Advertiser' ,'AdSource_Name', 'Inventory', 'Request',
                   'Impression', 'Revenue', 'Cost', 'Profit']

    labels = {"Network/publisher Id": "Pub_id",
              "Network/publisher Name": "Pub_Name",
              "Publisher Channel Id": "Pub_Channel_id",
              "Publisher Channel Name": "Pub_channel_Name",
              "Channel Name": "Channel_Name",
              "Ad Source Name" : "AdSource_Name",
              "Advertiser Id" : "Advertiser"}

    df.rename(columns={"Publisher Name": "Network/publisher Name"}, inplace=True)
    df.rename(columns=labels, inplace=True)
    df = df.reindex(columns=orderedList)
    return df





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

    response2 = req.get(url, cookies=token['data'])
    print(response2.status_code)
    data_json = response2.json()
    df = pd.DataFrame.from_dict(data_json['data'])
    df = alterColumns_pub(df)
    return df

print(connector())
# print(alterColumns_pub(['Channel Name', 'Cost', 'Impression', 'Inventory', 'Network/publisher Id', 'Profit', 'Publisher Channel Id', 'Publisher Channel Name', 'Publisher Name', 'Request', 'Revenue']))