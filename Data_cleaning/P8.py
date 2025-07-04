import pandas as pd
import re
dataset=pd.read_csv(r'C:\Users\arind\Downloads\cleaned_laptopdata.csv')
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
# dataset=dataset.drop('Memory',axis=1)
# dataset=dataset.to_csv(r'C:\Users\arind\Downloads\cleaned_laptopdata.csv')
# print(dataset.info)

# GPU
a=dataset['Gpu'][0]
def gpu_company(a):
    match=re.search(r'AMD|Intel|Nvidia',a,re.IGNORECASE)
    return match[0] if match else "Unknown"
dataset['Gpu_company']=dataset['Gpu'].apply(gpu_company)
# print(dataset['Gpu_company'].head(50))
def gpu_series(a):
    match =re.search(r'\b(?!AMD\b|Intel\b|Nvidia\b)(?:[A-Za-z]+\s?)+\b',a,re.IGNORECASE)
    return match[0] if match else "Unknown"
dataset['Gpu_series']=dataset['Gpu'].apply(gpu_series)
# print(dataset['Gpu_series'].head(55))
def gpu_version(a):
    match=re.search(r'\w+\d+\w+',a,re.IGNORECASE)
    return match[0] if match else None
dataset['Gpu_version']=dataset['Gpu'].apply(gpu_version)
# print(dataset['Gpu_version'].head(50))
print(dataset.head(50))

dataset=dataset.to_csv(r'C:\Users\arind\Downloads\cleaned_laptopdata.csv')