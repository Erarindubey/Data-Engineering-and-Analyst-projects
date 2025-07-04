import pandas as pd
df=pd.read_csv(r'C:\Users\arind\Downloads\surat_cleaned3.csv')
pd.set_option('display.max_columns',None)
# print(df.head(5))
# Price = Area*price_per_sqft

df['Area']=df['Area'].astype(int)
df['Price(₹)']=df['Area']*df['price_per_sqft(₹)']

print(df['Price(₹)'].head(50))

df=df.to_csv(r'C:\Users\arind\Downloads\surat_cleaned3.csv')
print('saved')