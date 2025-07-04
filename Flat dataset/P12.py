import re

import pandas as pd
df=pd.read_csv(r'C:\Users\arind\Downloads\surat_cleaned2.csv')
pd.set_option('display.max_columns',None)


# price/sqft

# Initialization
a=df['price_per_sqft'][0]

# retrieve digits

def digit(a):
    match=re.findall(r'\d+,\d+\s(?=per)',a)
    return match[0].replace(',','')
df['price_per_sqft(₹)']=df['price_per_sqft'].apply(digit)

print(df['price_per_sqft(₹)'].head(50))
print(df['price_per_sqft(₹)'].isnull().sum())
df=df.to_csv(r'C:\Users\arind\Downloads\surat_cleaned2.csv')
print('saved')