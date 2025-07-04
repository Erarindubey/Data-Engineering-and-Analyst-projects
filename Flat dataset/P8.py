import pandas as pd

df=pd.read_csv(r'C:\Users\arind\Downloads\surat_cleaned2.csv')
pd.set_option('display.max_columns',None)

df=df.dropna()

print(df.isnull().sum())
print(df.head(50))

df=df.to_csv(r'C:\Users\arind\Downloads\surat_cleaned2.csv')
print('saved successfully')
