import pandas as pd
import re
import numpy as np
df=pd.read_csv(r'C:\Users\arind\Downloads\swiggy_scrap_uncleaned.csv')
pd.set_option('display.max_columns',None)

# adjusting values after -

# removing months and year

a=df['Delivery_time(mins)'][0]

def Delivery(a):
    match=re.search(r'\d+(?=-)',a,re.IGNORECASE)
    return match.group(0) if match else 0
df['val1']=df['Delivery_time(mins)'].apply(Delivery).astype(int)
# print(df['val1'].head(50))

def Delivery2(a):
    match=re.search(r'\-(\d+)',a,re.IGNORECASE)
    return match[1] if match else 0
df['val2']=df['Delivery_time(mins)'].apply(Delivery2).astype(int)
# c=df['val2'][0]
# print(df['val2'].iloc[10:60])
df['Avg']=np.where(
    df['val2']!=0,
    (df['val1']+df['val2'])/2,
    df['val1']
)
df['Avg']=df['Avg'].astype(float)
print(df['Avg'].iloc[60:110])


df=df.to_csv(r'C:\Users\arind\Downloads\swiggy_scrap_uncleaned.csv')
print('saved')
