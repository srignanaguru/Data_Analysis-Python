import pandas as pd
import csv
df=pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv',
               converters={'medv': lambda x: 'High' if float(x) > 25 else 'Low'}
               )

with open('BostonHousing.csv','r') as f:
    reader=csv.reader(f)
    out=[]
    for i, row in enumerate(reader):
        if i>0:
            row[13]='High' if  float(row[13]) > 25 else 'Low'
        out.append(row)

df=pd.DataFrame(out[1:], columns=out[0])
print(df.head())