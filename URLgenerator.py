import datetime
import time
from AniviewReporting.reportType import reporttype

def customdate():
    dates = []
    for i in range(1, 3):
        date_entry = input('Enter a date in YYYY-MM-DD format')
        year, month, day = map(int, date_entry.split('-'))
        date = datetime.date(year, month, day)
        i += 1
        dates.append(date)

    return dates


def dategen(period = input("Please enter Date range")):

    today = datetime.date.today()
    if period == "yesterday":
        startdate = today.replace(day=(today.day - 1))
        enddate = today.replace(day=(today.day - 1))

    elif period == "last month":
        lastmonth = today.replace(day=1) - datetime.timedelta(days=1)
        startdate = today.replace(year= lastmonth.year,month=lastmonth.month, day=1)
        enddate = lastmonth

    elif period == "today":
        startdate = today
        enddate = today

    elif period == "month to date":
        startdate = today.replace(day=1)
        enddate = today

    elif period == "last 7 days":
        startdate = today - datetime.timedelta(days=7)
        enddate = today - datetime.timedelta(days=1)

    elif period == "custom range":
        dates = customdate()
        startdate = dates[0]
        enddate = dates[1]

    else:
        return "Please Spell the requirement correctly!"


    print("Today:" + str(today))
    print("start date:" + str(startdate))
    print("end date:" + str(enddate))



    return int(time.mktime(startdate.timetuple())),int(time.mktime(enddate.timetuple()))




def urlgen():
    baseurl = "http://manage.aniview.com/api/adserver/stats/report?"
    start_date,end_date = dategen()

    startdate = "startDate=" + str(start_date) + "&"
    # print(start_date)
    enddate = "endDate=" + str(end_date) + "&"
    # print(end_date)


    # dimensions = "dimensions="+"daily"+ "%2C" + "iid"+"%2C"+"iname"+ "%2C" + "ncidName"+ "%2C" +"pcid"+"%2C"+"pcidName"+ "%2C" + "aid" + "%2C" + "nasidName" + "&"
    #
    # # print(dimensions)
    # metrics = "metrics=" + "inventory"+"%2C"+"request"+"%2C"+"impression"+"%2C"+"revenue"+"%2C"+"cost"+"%2C"+"profit" + "&"
    #
    # query = "query=%7B%7D"
    #
    # file_format = "format=json" + "&"

    fields = reporttype()

    url = baseurl + startdate + enddate + fields
    print(url)

    return url

# print(dategen())
urlgen()
