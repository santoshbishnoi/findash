import datetime as dt


# print(dt.date.today().year)
# print(dt.time.now())

# chart_end_time=dt.datetime(dt.date.today().year, dt.date.today().month, dt.date.today().day, hour=15, minute=30, second=0)
# print(dt.datetime(dt.date.today().year, dt.date.today().month, dt.date.today().day, hour=15, minute=25, second=0)-dt.timedelta(days=1))
# time_behind=24
# hours_subracted=dt.timedelta(hours=time_behind)
# chart_open_time=chart_end_time-hours_subracted


# print(dt.datetime.now().weekday())


# print(dt.time(hour=1,minute=30, second=0, microsecond=0 )>dt.time(hour=15,minute=30, second=0, microsecond=0 ))

# current_time=dt.datetime.now()
# time_ahead=1
# time_behind=48
# hours_added=dt.timedelta(hours=time_ahead)
# hours_subracted=dt.timedelta(hours=time_behind)
# chart_end_time=current_time+hours_added
# chart_open_time=current_time-hours_subracted

# print(chart_open_time)
# print(chart_end_time)



# print((dt.datetime.now().date())+dt.timedelta(hours=1, minutes=30))
# print(type(dt.date.today()))
print(dt.datetime.now().time() < dt.time(hour=9,minute=15, second=0, microsecond=0))

dict(values=["2021-05-13"]),