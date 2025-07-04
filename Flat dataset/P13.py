import re

import pandas as pd
df=pd.read_csv(r'C:\Users\arind\Downloads\surat_cleaned2.csv')
pd.set_option('display.max_columns',None)
# print(df.head(50))

# price
# Intialization
a=df['price'][0]

def normalization(a):
    pattern1=r'\d+.\d+\s(?=Cr)'
    pattern2=r'\d+\s(?=Cr)'
    pattern3=r'\d+.\d+\s(?=Lac)'
    pattern4=r'\d+\s(?=Lac)'
    if re.search(pattern1,a,re.IGNORECASE):
        match=re.search(pattern1,a,re.IGNORECASE).group()
        return int(float(match)*10000000)
    elif re.search(pattern2,a,re.IGNORECASE):
        match=re.search(pattern2,a,re.IGNORECASE).group()
        return int(match)*10000000
    elif re.search(pattern3,a,re.IGNORECASE):
        match=re.search(pattern3,a,re.IGNORECASE).group()
        return int(float(match.replace('.',''))*10000)
    elif re.search(pattern4,a,re.IGNORECASE):
        match=re.search(pattern4,a,re.IGNORECASE).group()
        return int(match)*100000
    else:
        return ''
df['Price(₹)']=df['price'].apply(normalization)
print(df['Price(₹)'].iloc[1030:1090])

df=df.to_csv(r'C:\Users\arind\Downloads\surat_cleaned2.csv')
print('saved')