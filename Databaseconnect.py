import pymysql as psql
from pandas.io import sql





payload = {"host" : "thrivehq.cusrikqjbmvm.us-east-1.rds.amazonaws.com",
            "pnum" : 3306,
            "dbname": "Ads_txt",
            "id": "Thriveplus2017",
            "pwd":  "321happy"}

conn = psql.connect(host = payload["host"],port = payload["pnum"], user = payload["id"], passwd = payload["pwd"], db = payload["dbname"])
connect = conn.cursor()