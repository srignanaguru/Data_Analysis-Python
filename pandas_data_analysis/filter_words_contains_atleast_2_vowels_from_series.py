import pandas as pd

ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])

from collections import Counter

mask=ser.map(lambda x: sum([Counter(x.lower()).get(i, 0) for i in list('aeiou')])>=2)
res=ser[mask]

print(res)