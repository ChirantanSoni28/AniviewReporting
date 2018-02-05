import sqlalchemy as sql
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import pandas as pd
from AniviewReporting.APIconnection import connector
from sqlalchemy.sql import text



payload = {"host" : "@thrivehq.cusrikqjbmvm.us-east-1.rds.amazonaws.com",
            "pnum" : "3306/",
            "dbname": "Aniview",
            "id": "Thriveplus2017",
            "pwd":  "321happy"}

url = "mysql+pymysql://"+payload['id']+":"+payload['pwd']+payload['host']+":"+payload['pnum']+payload['dbname']
# print(url)

data = connector()


engine = sql.create_engine(url)
connection = engine.connect()

sqlConnect = data.to_sql(name='Publishers', con=connection, if_exists='replace', index=False)



