import pandas as pd
df=pd.read_csv(r'C:\Users\arind\Downloads\retail_store_sales.csv')
pd.set_option('display.max_columns',None)
# print(df.head(50))

print(df.describe())
# print(df.info())
print(df.isnull().sum())