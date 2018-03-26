from crontab import CronTab

users_cron = CronTab(user='chirantansoni')

job_Pubreport = users_cron.new(command='/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chirantansoni/PycharmProjects/AniviewReporting/Databaseconnect.py PublisherReport monthtodate')
job_Pubreport.minute.every(1)

job_Adsourcereport = users_cron.new(command='/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chirantansoni/PycharmProjects/AniviewReporting/Databaseconnect.py AdsourceReport monthtodate')
job_Adsourcereport.minute.every(1)

job_WaterfallReport = users_cron.new(command='/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/chirantansoni/PycharmProjects/AniviewReporting/Databaseconnect.py WaterfallOptimization monthtodate')
job_WaterfallReport.minute.every(1)

users_cron.write()