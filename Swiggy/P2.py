import pandas as pd
import re
df=pd.read_csv(r'C:\Users\arind\Downloads\swiggy_scrap_uncleaned.csv')
pd.set_option('display.max_columns',None)
# print(df.head(50))

# Rating and delivery_time

# retrieve numbers before '•'

# initialize
a=df['rating_and_delivery_time'][0]

def rating(a):
    match=re.search(r'\d+(\.\d+)?\s+(?=•)',a,re.IGNORECASE)
    return match[0] if match else None
df['Rating(out of 5)']=df['rating_and_delivery_time'].apply(rating).astype(float)

# print(df['Rating(out of 5)'].head(50))

# retrieve delivery time

def delivery(a):
    match=re.search(r'\d+(\-\d+)?\s+(?=mins)',a,re.IGNORECASE)
    return match[0] if match else None
df['Delivery_time(mins)']=df['rating_and_delivery_time'].apply(delivery)

print(df['Delivery_time(mins)'].head(50))
print(df['Delivery_time(mins)'].isnull().sum())

df=df.to_csv(r'C:\Users\arind\Downloads\swiggy_scrap_uncleaned.csv')
print('saved')