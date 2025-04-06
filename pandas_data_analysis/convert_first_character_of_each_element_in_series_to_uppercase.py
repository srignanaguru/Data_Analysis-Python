import pandas as pd
ser = pd.Series(['how', 'to', 'kick', 'ass?'])

res=ser.str.capitalize()

print(res)