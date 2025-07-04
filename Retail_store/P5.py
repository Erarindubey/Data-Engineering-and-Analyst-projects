import pandas as pd
from SaveFunction import save_to_csv

df=pd.read_csv(r'C:\Users\arind\Downloads\retail_store_sales_cleaned.csv')
pd.set_option('display.max_columns',None)

# Discount

df['Discount Applied']=df['Discount Applied'].fillna(False)

# print(df['Discount Applied'].head(50))
df['Quantity']=df['Quantity'].astype(int)
print(df.dtypes)

save_to_csv(df,r'C:\Users\arind\Downloads\retail_store_sales_cleaned.csv')