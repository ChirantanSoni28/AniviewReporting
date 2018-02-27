import requests as req
import pandas as pd
from AniviewReporting.URLgenerator import urlgen
from AniviewReporting.reportType import reporttype

"""The Below function sorts the column of a dataframe as required in the reports"""


def alterColumns(df):

    global orderedList, labels

    df.rename(columns={"Publisher Name": "Network/publisher Name"}, inplace=True)
    # print(type(df))
    # print(df.columns.tolist())

    if df.columns.tolist() == ['Channel Name', 'Cost', 'Date', 'Impression', 'Inventory', 'Network/publisher Id', 'Profit',
                               'Publisher Channel Id', 'Publisher Channel Name', 'Network/publisher Name', 'Request', 'Revenue']  \
            or df.columns.tolist() == ['Channel Name', 'Cost', 'Date', 'Impression', 'Inventory', 'Network/publisher Id', 'Network/publisher Name',
                                       'Profit', 'Publisher Channel Id', 'Publisher Channel Name', 'Request', 'Revenue']:

        orderedList = ['Date', 'Pub_id', 'Pub_Name', 'Pub_Channel_id', 'Pub_channel_Name', 'Channel_Name',
                       'Inventory', 'Request', 'Impression', 'Revenue', 'Cost', 'Profit']

        labels = {"Network/publisher Id": "Pub_id",
                  "Network/publisher Name": "Pub_Name",
                  "Publisher Channel Id": "Pub_Channel_id",
                  "Publisher Channel Name": "Pub_channel_Name",
                  "Channel Name": "Channel_Name",
                  }

    elif df.columns.tolist() == ['Ad Source Name', 'Advertiser Id', 'Cost', 'Date', 'Impression', 'Inventory',
                                 'Network/publisher Id', 'Profit', 'Publisher Channel Id', 'Publisher Channel Name',
                                 'Request', 'Revenue']:

        orderedList = ['Date', 'Pub_id', 'Pub_Channel_id', 'Pub_channel_Name',
                       'AdSource_Name', 'Advertiser', 'Inventory', 'Request',
                       'Impression', 'Revenue', 'Cost', 'Profit']

        labels = {"Network/publisher Id": "Pub_id",
                  "Publisher Channel Id": "Pub_Channel_id",
                  "Publisher Channel Name": "Pub_channel_Name",
                  "Ad Source Name": "AdSource_Name",
                  "Advertiser Id": "Advertiser"
                  }

    elif df.columns.tolist() == ['Ad Source Name', 'AdLoaded', 'Advertiser Id', 'Bid', 'Date', 'Impression',
                                 'Inventory', 'Network/publisher Id', 'Publisher Channel Id', 'Request']:

        orderedList = ['Date', 'Pub_id', 'Pub_Channel_id', 'AdSource_Name', 'Advertiser', 'Inventory', 'Request',
                       'Impression', 'Bid', 'AdLoaded']

        labels = {"Network/publisher Id": "Pub_id",
                  "Publisher Channel Id": "Pub_Channel_id",
                  "Ad Source Name": "AdSource_Name",
                  "Advertiser Id": "Advertiser"
                  }


    df.rename(columns=labels , inplace=True)
    df = df.reindex(columns=orderedList)

    return df


def connector():
    payload = {
        "id": "chirantan@thrive.plus",
        "password": "changeme"
    }
    response = req.post('http://manage.aniview.com/api/token?format=json', json=payload)

    # print(response.status_code)
    # print(response.text)
    token = response.json()
    # print(token['data'])
    url = urlgen()

    response2 = req.get(url, cookies=token['data'])
    print(response2.status_code)
    data_json = response2.json()
    df = pd.DataFrame.from_dict(data_json['data'])
    # print(df.columns.tolist())

    df = alterColumns(df)
    return df


print(connector())
# print(alterColumns_pub(['Channel Name', 'Cost', 'Impression', 'Inventory', 'Network/publisher Id', 'Profit', 'Publisher Channel Id', 'Publisher Channel Name', 'Publisher Name', 'Request', 'Revenue']))
