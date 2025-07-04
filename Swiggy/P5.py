import pandas as pd
df=pd.read_csv(r'C:\Users\arind\Downloads\swiggy_scrap_uncleaned.csv')
pd.set_option('display.max_columns',None)
# print(df.head(50))
df=df[['hotel_name','location','food_type','Rating(out of 5)','Delivery_time(mins)','offer']].drop_duplicates()
print(df[['hotel_name','location','food_type','Rating(out of 5)','Delivery_time(mins)','offer']].duplicated().sum())

df=df.to_csv(r'C:\Users\arind\Downloads\swiggy_uncleaned.csv')
print('saved')