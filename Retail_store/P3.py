from unittest.mock import inplace

import pandas as pd
from SaveFunction import save_to_csv
df=pd.read_csv(r'C:\Users\arind\Downloads\retail_store_sales_cleaned.csv')
pd.set_option('display.max_columns',None)

# Remove Na from quantity

df_clean=df.dropna(subset=['Quantity'])

print(df_clean['Quantity'].head(50))

save_to_csv(df_clean,r'C:\Users\arind\Downloads\retail_store_sales_cleaned.csv')