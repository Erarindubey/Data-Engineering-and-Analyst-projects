import pandas as pd
import re
from SaveFunction import save_to_csv
df=pd.read_csv(r'C:\Users\arind\Downloads\swiggy_uncleaned.csv')
pd.set_option('display.max_columns', None)
a=df['off(%)'][0]
def remove(a):
    return re.sub(r'%','',a,re.IGNORECASE)
df['off(%)']=df['off(%)'].apply(remove)
b=df['off(₹)'][0]
def remove2(b):
    return re.sub(r'₹','',b,re.IGNORECASE)
df['off(₹)']=df['off(₹)'].apply(remove2)
df['off(%)']=df['off(%)'].astype(int)
df['off(₹)']=df['off(₹)'].astype(int)
print(df[['off(%)','off(₹)']].head(50))

save_to_csv(df,r'C:\Users\arind\Downloads\swiggy_uncleaned.csv')
