import pandas as pd

ser = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2012'])

from dateutil.parser import parse

ser_ts=ser.map(lambda x: parse(x))

ser_datestr=ser_ts.dt.year.astype('str') + '-' + ser_ts.dt.month.astype('str') + '-' + '04'

res=[parse(i).strftime('%Y-%m-%d') for i in ser_datestr]

out=ser.map(lambda x: parse('04' + x))
print(out)