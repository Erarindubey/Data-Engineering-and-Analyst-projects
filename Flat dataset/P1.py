import pandas as pd
df=pd.read_csv(r'C:\Users\arind\Downloads\surat_uncleaned.csv')
pd.set_option('display.max_columns',None)
df=df.dropna()
df=df.to_csv(r'C:\Users\arind\Downloads\surat_cleaned.csv',index=False)
# print(df.isnull().sum())
print('saved successfully')