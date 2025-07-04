import re

import pandas as pd
df=pd.read_csv(r'C:\Users\arind\Downloads\surat_cleaned.csv')
pd.set_option('display.max_columns',None)
# print(df.head(50))

# Square feet
x=df['square_feet'][0]
def square_feet2(x):
    if 'sqft' in x:
        return x.replace('sqft','')
    else:
        return x
df['Area']=df['square_feet'].apply(square_feet2)
def square_feet(x):
    x=x.replace(',','')
    if 'sqyrd' in x:
        return float(x.split()[0])*9
    if 'sqm' in x:
        return float(x.split()[0])*10.7639
    if 'ground' in x:
        return float(x.split()[0])*2400
    else:
        return x
df['Area']=df['Area'].apply(square_feet).astype(float)
# print(df['Area'].iloc[:60])

# checkk=df[~df['square_feet'].str.contains('sqft',case=False)]
# print(checkk.head(50))

df=df.drop('square_feet',axis=1)
df=df.to_csv(r'C:\Users\arind\Downloads\surat_cleaned.csv')
print('saved successfully')