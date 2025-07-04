import pandas as pd
import re
from matplotlib.dates import datestr2num

dataset=pd.read_csv(r'C:\Users\arind\Downloads\cleaned_laptopdata.csv')
pd.set_option('display.max_columns',None)
# pd.set_option('display.max.rows',None)
#Memory

#Step 1 Remove Primary memory size
a=dataset['Memory']
def memory1(a):
    match=re.findall(r'\d+(?=GB|TB)',a,re.IGNORECASE)
    return match[0] if match else 'Unknown'
dataset['Memory1']=dataset['Memory'].apply(memory1).astype(int)
b=dataset['Memory1'][0]
# print(dataset['memory1'].head(50))

# Step2 Remove Primary memory type

def memory1_type(a):
    match=re.search(r'(?!GB|TB)\s+(SSD|HDD|Hybrid|Flash\s\w+)',a,re.IGNORECASE)
    return match[0] if match else 'Unknown'
dataset['Memory1_type']=dataset['Memory'].apply(memory1_type)
# print(dataset['memory1_type'].head(50))

# Step3 Remove Secondary memory size

def memory2(a):
    match=re.search(r'\s*\s+\d+(?=GB|TB)',a,re.IGNORECASE)
    return match[0] if match else 0
dataset['Memory2']=dataset['Memory'].apply(memory2).astype(int)
# print(dataset['Memory2'].head(60))

# Step4 Remove Secondary memory type

def memory2_type(a):
    after_plus=re.split(r'\s*\+\s*',a)[1:]
    match=r'\b(SSD|HDD|Hybrid|Flash\s\w+)'
    matches=[]
    for part in after_plus:
        matches.extend(re.findall(match,part,re.IGNORECASE))
    return ' '.join(matches) if matches else 'NA'
dataset['Memory2_type']=dataset['Memory'].apply(memory2_type)
# print(dataset['Memory2_type'][500:900])

# Step5 Normalize values

# print(dataset[['memory1','memory1_type','Memory2','Memory2_type']].head(50))
def multiply(value):
    if value <10:
        return value*1024
    else:
        return value
dataset['Memory1']=dataset['Memory1'].apply(multiply)
dataset['Memory2']=dataset['Memory2'].apply(multiply)
# print(dataset[['memory1','Memory2']].head(50))
# print(dataset['Memory2'].dtypes)

# Step6 Calculate total memory

dataset['Total_memory']=dataset['Memory1']+dataset['Memory2']
# print(dataset['Total_memory'].head(50))
# print(dataset[['memory1_type','Memory2_type']].head(50))

print(dataset.info)

# Step7 Save

dataset=dataset.to_csv(r'C:\Users\arind\Downloads\cleaned_laptopdata.csv')

print('Saved successfully ')