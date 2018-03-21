import sys
import sqlalchemy as sql
# import pexpect, sys
from APIconnection import connector



payload = {"host" : "@thrivehq.cusrikqjbmvm.us-east-1.rds.amazonaws.com",
            "pnum" : "3306/",
            "dbname": "Aniview",
            "id": "Thriveplus2017",
            "pwd":  "321happy"}

data = connector()



def mysql_connect(credentials):

    url = "mysql+pymysql://" + credentials['id'] + ":" + credentials['pwd'] + credentials['host'] + ":" + \
                  credentials['pnum'] + credentials['dbname']
    # print(url)


    engine = sql.create_engine(url)
    connection = engine.connect()

    return connection



def typeOfreport():


    if data.columns.tolist() == ['Date', 'Pub_id', 'Pub_Name', 'Pub_Channel_id',
                                 'Pub_channel_Name', 'Channel_Name', 'Inventory', 'Request', 'Impression', 'Revenue', 'Cost', 'Profit']:

        type = "Publisher Report"

    elif data.columns.tolist() == ['Date', 'Pub_id', 'Pub_Channel_id', 'Pub_channel_Name',
                                   'AdSource_Name', 'Advertiser', 'Inventory', 'Request', 'Impression', 'Revenue', 'Cost', 'Profit']:

        type = "Adsource Report"

    elif data.columns.tolist() == ['Date', 'Pub_id', 'Pub_Channel_id', 'AdSource_Name',
                                   'Advertiser', 'Inventory', 'Request', 'Impression', 'Bid', 'AdLoaded']:

        type = "Waterfall Optimization"

    return type


def tableSelect():

    reportType = typeOfreport()

    connection = mysql_connect(payload)

    if reportType == "Publisher Report":
        # print("PR")
        sqlConnect = data.to_sql(name='PublisherReport', con=connection, if_exists='replace', index=False)

    elif reportType == "Adsource Report":
        # print("AR")
        sqlConnect = data.to_sql(name='AdsourceReport', con=connection, if_exists='replace', index=False)

    elif reportType == "Waterfall Optimization":
        # print("WO")
        sqlConnect = data.to_sql(name='WaterfallOptimization', con=connection, if_exists='replace', index=False)

    return sqlConnect



tableSelect()