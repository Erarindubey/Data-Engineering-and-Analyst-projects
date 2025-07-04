import pandas as pd
from SaveFunction import save_to_csv
df=pd.read_csv(r'C:\Users\arind\Downloads\retail_store_sales_cleaned.csv')
pd.set_option('display.max_columns',None)

# Price_per_unit

# df['M2']=df['Price Per Unit'].fillna(0)
# df['M3']=df['Quantity']
# df['M']=df['M2']*df['M3']
# print(df['M'].head(50))

# Spent

df['D2']=df['Quantity']
df['D3']=df['Total Spent'].fillna(0)
df['D']=df['D3']/df['D2']
# print(df['D'].head(50))
print(df['Price Per Unit'].head(50))
# print(df['Price Per Unit'].isnull().sum())
df['Price Per Unit']=df['Price Per Unit'].fillna(0)
df['Price Per Unit']=df.apply(lambda x:x['D'] if x['Price Per Unit']==0 else x['Price Per Unit'],axis=1)

# print(df['Price Per Unit'].head(50))
df=df.drop('D3',axis=1)
df=df.drop('D2',axis=1)
df=df.drop('D',axis=1)

# print(df.head(50))

# print(df['Price Per Unit'].isnull().sum())

save_to_csv(df,r'C:\Users\arind\Downloads\retail_store_sales_cleaned.csv')