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

    response2 = req.get(url, cookies=token['data'])
    print(response2.status_code)
    data = response2.json()
    df = pd.DataFrame.from_dict(data['data'])
    print(df)
    # writer = pd.ExcelWriter('/Users/chirantansoni/Desktop/data.xlsx')
    # df.to_excel(writer)
    # writer.save()



connector()
