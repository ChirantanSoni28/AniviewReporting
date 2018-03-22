import sqlalchemy as sql
from APIconnection import connector



payload = {"host" : "",
            "pnum" : "",
            "dbname": "",
            "id": "",
            "pwd":  ""}

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
        print("Publisher Report")
        sqlConnect = data.to_sql(name='PublisherReport', con=connection, if_exists='replace', index=False)

    elif reportType == "Adsource Report":
        print("Adsource Report")
        sqlConnect = data.to_sql(name='AdsourceReport', con=connection, if_exists='replace', index=False)

    elif reportType == "Waterfall Optimization":
        print("Waterfall Optimization Report")
        sqlConnect = data.to_sql(name='WaterfallOptimization', con=connection, if_exists='replace', index=False)

    return sqlConnect



# process = pexpect.spawn('Databaseconnect.py')
# process.expect("Please enter the Report type")
# process.sendline("Publisher Report")

# databaseSelect()
# print(typeOfreport())
# mysql_connect(payload)

tableSelect()
