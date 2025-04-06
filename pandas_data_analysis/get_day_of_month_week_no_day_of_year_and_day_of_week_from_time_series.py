import pandas as pd

ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])

from dateutil.parser import parse

df=ser.map(lambda x: parse(x))

res=pd.to_datetime(df)

print("Date: ",res.dt.day.tolist())
print("Week number: ",res.dt.weekday.tolist())
print("Day number of year: ", res.dt.day_of_year.tolist())
print("Day of week: ", res.dt.day_of_week.tolist())

