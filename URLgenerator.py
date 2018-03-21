
from reportType import reporttype
from dateGen import dategen





def urlgen():
    baseurl = "http://manage.aniview.com/api/adserver/stats/report?"
    start_date,end_date = dategen()

    startdate = "startDate=" + str(start_date) + "&"
    # print(start_date)
    enddate = "endDate=" + str(end_date) + "&"
    # print(end_date)

    fields = reporttype()

    url = baseurl + startdate + enddate + fields
    print(url)

    return url


# print(urlgen())



