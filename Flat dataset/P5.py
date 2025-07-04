import pandas as pd
import re

df=pd.read_csv(r'C:\Users\arind\Downloads\surat_cleaned.csv')
pd.set_option('display.max_columns', None)

# Initialization

a=df['transaction'][0]
b=df['status'][0]
c=df['floor'][0]
d=df['furnishing'][0]
e=df['facing'][0]

# Transaction

# Digits
def misplaced_values(a):
    match=re.search(r'(\d*)',a)
    return match[0] if match else a
df['Mv1']=df['transaction'].apply(misplaced_values)

# Furnished

def furnish(a):
    if re.findall(r'\b(Furnished|Unfurnished|Semi\-Furnished)\b',a,re.IGNORECASE):
        return a
    else:
        return ''
df['Mv2']=df['transaction'].apply(furnish)

# Clean transaction

def transaction(a):
    if re.search(r'(New\sProperty|Resale)',a,re.IGNORECASE):
        return a
    else:
        return ''
df['transaction']=df['transaction'].apply(transaction)

# Status

# Property

def transaction2(b):
    if re.search(r'(New\sProperty|Resale)',b,re.IGNORECASE):
        return b
    else:
        return ''
df['Mv3']=df['status'].apply(transaction2)

# out of

def status(b):
    if re.search(r'\d*\s(out\sof)\s\d*',b,re.IGNORECASE):
        return b
    # elif re.findall(r'\b\d+(?:\.\d+)?\s*[Xx]\s*\d+(?:\.\d+)?\b',b,re.IGNORECASE):
    #     return b
    else:
        return ''
df['Mv4']=df['status'].apply(status)

# size

def status2(b):
    match=re.findall(r'\b\d+(?:\.\d+)?\s*[Xx]\s*\d+(?:\.\d+)?\b',b,re.IGNORECASE)
    return match[0] if match else ''
df['Mv5']=df['status'].apply(status2)

# Clean status

def status3(b):
    if re.search(r'(New\sProperty|Resale|Freehold|Co\-operative)', b, re.IGNORECASE):
        return ''
    elif re.search(r'\d*\s(out\sof)\s\d*', b, re.IGNORECASE):
        return ''
    elif re.search(r'\b\d+(?:\.\d+)?\s*[Xx]\s*\d+(?:\.\d+)?\b', b, re.IGNORECASE):
        return ''
    else:
        return b
df['status'] = df['status'].apply(status3)

# Floor

# Property

def transaction3(c):
    if re.search(r'(New\sProperty|Resale)',c,re.IGNORECASE):
        return c
    else:
        return ''
df['Mv6']=df['floor'].apply(transaction3)

# Furnished

def furnish2(c):
    if re.findall(r'\b(Furnished|Unfurnished)\b',c,re.IGNORECASE):
        return c
    else:
        return ''
df['Mv7']=df['floor'].apply(furnish2)

# Clean Floor

def floor(c):
    if re.search(r'(New\sProperty|Resale)',c,re.IGNORECASE):
        return ''
    elif re.search(r'\b(?<!out of )\b\d+\b(?!\s*out of\s*\d+\b)',c,re.IGNORECASE):
        return ''
    elif re.search(r'\b(Furnished|Unfurnished)\b',c,re.IGNORECASE):
        return ''
    else:
        return c
df['floor']=df['floor'].apply(floor)

# Furnishing

# face

def direction(d):
    match=re.search(r'(North|South|West|East|North\s\-\sEast|South\s\-\sWest)',d,re.IGNORECASE)
    return match[0] if match else ''
df['Mv8']=df['furnishing'].apply(direction)

# clean furnishing

def furnishing(d):
    match=re.search(r'(Furnished|Unfurnished|Semi\-Furnished)',d,re.IGNORECASE)
    return match[0] if match else ''
df['furnishing']=df['furnishing'].apply(furnishing)

# Facing

# clean facing

def direction2(e):
    match=re.search(r'(North|South|West|East|North\s\-\sEast|South\s\-\sWest)',e,re.IGNORECASE)
    return match[0] if match else ''
df['facing']=df['facing'].apply(direction2)


# Misplaced values Columns
#                                Mv1==Digits from transaction
#                                Mv2==Furnish from transaction
#                                Mv3==Property from status
#                                Mv4==Out of from status
#                                Mv5=size from status
#                                Mv6==property from floor
#                                Mv7==Furnish from floor
#                                Mv8==direction from furnishing
#
#                                Mv2==Mv7==Furnishing
#                                Mv3==Mv6==Transaction
#                                Mv4==Floor
#                                Mv8==Facing
#
#
# Filling Furnishing
df['furnishing']=df.apply(lambda row:row['Mv2'] if row['furnishing']=='' else row['furnishing'],axis=1)
df['furnishing']=df.apply(lambda row:row['Mv7'] if row['furnishing']=='' else row['furnishing'],axis=1)

# Filling transaction
df['transaction']=df.apply(lambda row:row['Mv3'] if row['transaction']=='' else row['transaction'],axis=1)
df['transaction']=df.apply(lambda row:row['Mv6'] if row['transaction']=='' else row['transaction'],axis=1)

# Filling Floor
df['floor']=df.apply(lambda row:row['Mv4'] if row['floor']=='' else row['floor'],axis=1)

# Filling Facing
df['facing']=df.apply(lambda row:row['Mv8'] if row['facing']=='' else row['facing'],axis=1)

# empty_count=df['facing'].eq('').sum()
# print(empty_count)

# Saving

df=df.to_csv(r'C:\Users\arind\Downloads\surat_cleaned2.csv')
print('saved sucessfully')