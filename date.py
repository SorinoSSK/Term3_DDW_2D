from datetime import datetime
import pandas as pd

df = pd.read_csv('2Ddata.csv')
df['date'] = df.loc[:, "date"].apply(lambda data: (pd.to_datetime(data)))

date = datetime(2020,11,1)
df2 = df.loc[(df['day'] >= date),:].reset_index()
print(df2)

df2.to_csv('AfterNov.csv')
