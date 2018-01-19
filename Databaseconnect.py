import sqlalchemy
import pandas





payload = {"host" : "@thrivehq.cusrikqjbmvm.us-east-1.rds.amazonaws.com",
            "pnum" : "3306/",
            "dbname": "Aniview",
            "id": "Thriveplus2017",
            "pwd":  "321happy"}

url = "mysql+pymysql://"+payload['id']+":"+payload['pwd']+payload['host']+":"+payload['pnum']+payload['dbname']
# print(url)

engine = sqlalchemy.create_engine(url)
connection = engine.connect()
