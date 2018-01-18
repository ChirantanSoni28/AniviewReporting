import requests as req
import json
import ijson
import numpy as np
import pandas as pd
import My
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

    response2 = req.get(url, cookies=token['data'])
    print(response2.status_code)
    data = response2.json()
    df = pd.DataFrame.from_dict(data['data'])
    # print(df)
    # writer = pd.ExcelWriter('/Users/chirantansoni/Desktop/data.xlsx')
    # df.to_excel(writer)
    # writer.save()

    payload = {"host": "thrivehq.cusrikqjbmvm.us-east-1.rds.amazonaws.com",
               "pnum": 3306,
               "dbname": "Ads_txt",
               "id": "Thriveplus2017",
               "pwd": "321happy"}

    conn = psql.connect(host=payload["host"], port=payload["pnum"], user=payload["id"], passwd=payload["pwd"],
                        db=payload["dbname"])
    connect = conn.cursor()
    tosql = df.to_sql(df,conn, if_exists='append')
    print(tosql)

connector()
