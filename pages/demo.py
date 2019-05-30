import datetime
time = datetime.datetime.now().timetuple()
now_month = str(time.tm_mon)
print(now_month)