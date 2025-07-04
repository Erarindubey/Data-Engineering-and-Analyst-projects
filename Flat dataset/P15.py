import pandas as pd
df=pd.read_csv(r'C:\Users\arind\Downloads\surat_cleaned2.csv')
pd.set_option('display.max_columns',None)
df=df.reindex(columns=['areaWithType','transaction','poss_by(year)','Month','Floor_no','Total_floors','furnishing','facing','Property_type','Property_type2','Property_category','Property_location','Area','price_per_sqft(₹)','Price(₹)'])

print(df.dtypes)

df=df.to_csv(r'C:\Users\arind\Downloads\surat_cleaned3.csv')
print('saved')