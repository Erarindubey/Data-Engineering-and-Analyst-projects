import pandas as pd
import re
from SaveFunction import save_to_csv
df=pd.read_csv(r'C:\Users\arind\Downloads\swiggy_uncleaned.csv')
pd.set_option('display.max_columns', None)
# print(df.head(50))

# a=df['offer'][0]
df['off']=df['offer']
# print(df['off'].head(50))
a=df['off'][0]
# def off(a):
#     match=re.search(r'(?=₹)?\d+(?=%)?',a,re.IGNORECASE)
#     return match[0] if match else 0
# df['Off']=df['offer'].apply(off)
# print(df['Off'].head(50))

def off(a):
    match=re.search(r'\d+(%)\s*(?=OFF)',a,re.IGNORECASE)
    return match[0] if match else 0 
df['off(%)']=df['off'].apply(off)
def off2(a):
    match=re.search(r'(₹)\d+\s*(?=OFF)',a,re.IGNORECASE)
    return match[0] if match else 0
df['off(₹)']=df['off'].apply(off2)
print(df['off(%)'].head(50))
print(df['off(₹)'].head(50))

save_to_csv(df,r'C:\Users\arind\Downloads\swiggy_uncleaned.csv')
