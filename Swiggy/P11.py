import pandas as pd
from SaveFunction import save_to_csv
df=pd.read_csv(r'C:\Users\arind\Downloads\swiggy_uncleaned.csv')
pd.set_option('display.max_columns',None)

new_order=['hotel_name','location','food_type','Rating(out of 5)','Delivery_time(mins)','off(%)','off(₹)','Upto','Every_Items_at(₹)']
df=df[new_order]
print(df.head(50))

save_to_csv(df,r'C:\Users\arind\Downloads\swiggy_uncleaned.csv')