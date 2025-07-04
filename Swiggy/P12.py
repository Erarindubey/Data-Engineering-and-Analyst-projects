import pandas as pd
import re
from SaveFunction import save_to_csv
df=pd.read_csv(r'C:\Users\arind\Downloads\swiggy_uncleaned.csv')
pd.set_option('display.max_columns',None)
# df['Every_Items_at(₹)']=df['Every_Items_at(₹)'].astype(object)
df=df['Every_Items_at(₹)'].fillna('Not Available')
print(df.head(50))
save_to_csv(df,r'C:\Users\arind\Downloads\swiggy_uncleaned.csv')
