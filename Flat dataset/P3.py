import pandas as pd
import re
df=pd.read_csv(r'C:\Users\arind\Downloads\surat_cleaned.csv')
pd.set_option('display.max_columns', None)
# print(df.head(50))
# Property type
a=df['property_name'][0]
def property_type(a):
    match =re.search(r'\d+\s+(BHK)',a,re.IGNORECASE)
    return match[0] if match else 'NA'
df['Property_type']=df['property_name'].apply(property_type)
# print(df['Property_type'].head(50))

# Property Category
# r'(?! *BHK)[^0-9\sBHK]*\w*\s*\w*(?=\sfor)

def property_category(a):
    result=[]
    parts=a.split()
    for part in parts:
       if 'for' in part.lower():
           break
       if 'BHK' not in part and not part.isdigit():
           result.append(part)
    return ' '.join(result).strip()
df['Property_category']=df['property_name'].apply(property_category)
# print(df['Property_category'].iloc[:60])
# na_count=df[df['Property_category']=='NA'].shape[0]
# print(na_count)

# Property Location

def property_location(a):
    match=re.search(r'(?<=in\s)(\w+\s*)*',a,re.IGNORECASE)
    return match[0] if match else 'NA'
df['Property_location']=df['property_name'].apply(property_location)
# print(df['Property_location'].head(50))
df=df.drop('property_name',axis=1)
df=df.to_csv(r'C:\Users\arind\Downloads\surat_cleaned.csv')
print('saved successfully')