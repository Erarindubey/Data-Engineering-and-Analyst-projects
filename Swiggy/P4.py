import pandas as pd
df=pd.read_csv(r'C:\Users\arind\Downloads\swiggy_scrap_uncleaned.csv')
pd.set_option('display.max_columns',None)

df['Delivery_time']=df['Avg'].where(df['Avg']!=0,df['Delivery_time(mins)'])
# print(df['Deliver_time'].iloc[60:110])
df=df.drop('Delivery_time(mins)',axis=1)

df=df.rename(columns={'Delivery_time': 'Delivery_time(mins)'})
df=df.drop('val1',axis=1)
df=df.drop('val2',axis=1)
df=df.drop('Avg',axis=1)
print(df.head(50))
df=df.to_csv(r'C:\Users\arind\Downloads\swiggy_scrap_uncleaned.csv')
print('saved')
