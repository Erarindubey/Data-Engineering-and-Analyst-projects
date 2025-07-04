import pandas as pd
import re

df=pd.read_csv(r'C:\Users\arind\Downloads\surat_cleaned2.csv')
pd.set_option('display.max_columns',None)

# Floor

# initialize
a=df['floor'][0]

# first digit and ground retrieve

# dict

x={'Ground':0,'Lower Basement':-1}

# Function to retrieve digits

def digit1(a):
    match1=re.search(r'\d+\s(?=out)',a,re.IGNORECASE)
    return match1[0] if match1 else a
df['Floor_no']=df['floor'].apply(digit1)

b=df['Floor_no'][0]

# removing digits after ground/lower basement

def ground(b):
    match3=re.search(r'(Ground|Lower\sBasement)\s+(?=out)',b,re.IGNORECASE)
    return match3[0] if match3 else b
df['Floor_no']=df['Floor_no'].apply(ground)

# converting ground/basement to numerical value

def ground2(b,x):
    match2=('|').join(x.keys())
    return re.sub(match2, lambda m: str(x[m.group()]),b)
df['Floor_no']=df['Floor_no'].apply(lambda z: ground2(z,x)).astype(int)


# print(df['Floor_no'].iloc[110:170])

# search=df[df['Floor_no'] < 0]
# print(search)

# now retrieve digits after 'of' or in other words retrieve total floors

def total(a):
    match=re.search(r'of\s(\d+)',a,re.IGNORECASE)
    return match[1] if match else ''
df['Total_floors']=df['floor'].apply(total)
print(df['Total_floors'].head(50))
print(df['Total_floors'].isnull().sum())

df=df.to_csv(r'C:\Users\arind\Downloads\surat_cleaned2.csv')

print('saved')