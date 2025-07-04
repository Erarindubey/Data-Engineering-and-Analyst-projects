import pandas as pd
import re
df=pd.read_csv(r'C:\Users\arind\Downloads\surat_cleaned2.csv')
pd.set_option('display.max_columns',None)
# print(df.head(50))
# Retriving digits from property_type
# Initialize

a=df['Property_type'][0]

def digit(a):
    match=re.search(r'\d+\s(?=BHK)',a,re.IGNORECASE)
    return match[0] if match else ''

df['Property_type2']=df['Property_type'].apply(digit).astype(int)
# print(df['Property_type2'].head(20))
# print(df['Property_type2'].isnull().sum())

def bhk(a):
    match=re.search(r'(BHK)',a,re.IGNORECASE)
    return match[0] if match else ''
df['Property_type']=df['Property_type'].apply(bhk)

# print(df[['Property_type','Property_type2']].head(50))
print(df.dtypes)

df=df.to_csv(r'C:\Users\arind\Downloads\surat_cleaned2.csv')
print('saved')