import pandas as pd
from SaveFunction import save_to_csv
df=pd.read_csv(r'C:\Users\arind\Downloads\retail_store_sales.csv')
pd.set_option('display.max_columns',None)
# print(df['Item'].head(50))
df['Item']=df['Item'].fillna('Unknown')
print(df['Item'].head(50))
save_to_csv(df,r'C:\Users\arind\Downloads\retail_store_sales_cleaned.csv')
