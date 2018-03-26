import sqlalchemy as sql
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
        print("Publisher Report")
        sqlConnect = data.to_sql(name='PublisherReport', con=connection, if_exists='replace', index=False, dtype={'Date':sql.types.DATE,
                                                                                                                  'Pub_id':sql.types.VARCHAR(length=225),
                                                                                                                  'Pub_Name':sql.types.VARCHAR(length=225),
                                                                                                                  'Pub_Channel_id': sql.types.VARCHAR(length=225),
                                                                                                                  'Pub_channel_Name': sql.types.VARCHAR(length=225),
                                                                                                                  'Channel_Name': sql.types.VARCHAR(length=225),
                                                                                                                  'Inventory': sql.types.INTEGER(),
                                                                                                                  'Request': sql.types.INTEGER(),
                                                                                                                  'Impression': sql.types.INTEGER(),
                                                                                                                  'Revenue': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                                  'Cost': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                                  'Profit': sql.types.FLOAT(precision=4, asdecimal=True)})

    elif reportType == "Adsource Report":
        print("Adsource Report")
        sqlConnect = data.to_sql(name='AdsourceReport', con=connection, if_exists='replace', index=False, dtype={'Date':sql.types.DATE,
                                                                                                                  'Pub_id':sql.types.VARCHAR(length=225),
                                                                                                                  'Pub_Channel_id': sql.types.VARCHAR(length=225),
                                                                                                                  'Pub_channel_Name': sql.types.VARCHAR(length=225),
                                                                                                                 'AdSource_Name': sql.types.VARCHAR(225),
                                                                                                                 'Advertiser': sql.types.VARCHAR(225),
                                                                                                                 'Inventory': sql.types.INTEGER(),
                                                                                                                 'Request': sql.types.INTEGER(),
                                                                                                                 'Impression': sql.types.INTEGER(),
                                                                                                                 'Revenue': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                                 'Cost': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                                 'Profit': sql.types.FLOAT(precision=4, asdecimal=True)})

    elif reportType == "Waterfall Optimization":
        print("Waterfall Optimization Report")
        sqlConnect = data.to_sql(name='WaterfallOptimization', con=connection, if_exists='replace', index=False, dtype={'Date':sql.types.DATE,
                                                                                                                  'Pub_id':sql.types.VARCHAR(length=225),
                                                                                                                  'Pub_Channel_id': sql.types.VARCHAR(length=225),
                                                                                                                 'AdSource_Name': sql.types.VARCHAR(225),
                                                                                                                 'Advertiser': sql.types.VARCHAR(225),
                                                                                                                 'Inventory': sql.types.INTEGER(),
                                                                                                                 'Request': sql.types.INTEGER(),
                                                                                                                 'Impression': sql.types.INTEGER(),
                                                                                                                 'Bid': sql.types.INTEGER(),
                                                                                                                 'AdLoaded': sql.types.INTEGER()})

    return sqlConnect



# process = pexpect.spawn('Databaseconnect.py')
# process.expect("Please enter the Report type")
# process.sendline("Publisher Report")

# mysql_connect(payload)

tableSelect()