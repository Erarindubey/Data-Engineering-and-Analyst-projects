import pandas as pd
df=pd.read_csv(r'C:\Users\arind\Downloads\swiggy_scrap_uncleaned.csv')
pd.set_option('display.max_columns',None)
print(df.head(50))