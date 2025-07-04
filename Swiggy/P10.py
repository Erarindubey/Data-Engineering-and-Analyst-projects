import pandas as pd
import re
from SaveFunction import save_to_csv
df=pd.read_csv(r'C:\Users\arind\Downloads\swiggy_uncleaned.csv')
pd.set_option('display.max_columns', None)
a=df['offer'][0]
def items(a):
    match=re.search(r'(at|@)\s+₹(\d+)',a,re.IGNORECASE)
    return match[2] if match else ''
df['Every_Items_at(₹)']=df['offer'].apply(items)
def items2(a):
    match=re.search(r'Free',a,re.IGNORECASE)
    return 0 if match else ''
df['temp']=df['offer'].apply(items2)
print(df['temp'].head(50))
df['Every_Items_at(₹)']=df.apply(lambda x:x['temp'] if x['Every_Items_at(₹)']=='' else x['Every_Items_at(₹)'],axis=1)
df=df.drop('temp',axis=1)
df=df.drop('off',axis=1)
df=df.drop('offer',axis=1)
print(df['Every_Items_at(₹)'].head(50))

save_to_csv(df,r'C:\Users\arind\Downloads\swiggy_uncleaned.csv')