import pandas as pd
import re
from SaveFunction import save_to_csv
df=pd.read_csv(r'C:\Users\arind\Downloads\swiggy_uncleaned.csv')
pd.set_option('display.max_columns',None)
# print(df['offer'].head(50))

# we gonna retrieve and clean Offer column 
# for that we need to remove percentage values and values which are in rupees
a=df['offer'][0]
def upto(a):
    match=re.search(r'(?:above|upto\s+\₹)\b(.*)',a,re.IGNORECASE)
    return match[1].strip() if match else None
df['Upto']=df['offer'].apply(upto)
b=df['Upto'][0]
def remove(b):
    return re.sub(r'₹','',b) if b else None
df['Upto']=df['Upto'].apply(remove)
print(df['Upto'].head(50))
df['Upto'].fillna(0,inplace=True)
print(df['Upto'].head(50))
save_to_csv(df,'swiggy_uncleaned.csv')
print('saved successfully')
