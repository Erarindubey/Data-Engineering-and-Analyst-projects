import pandas as pd
dataset=pd.read_csv(r'C:\Users\arind\Downloads\cleaned_laptopdata.csv')
dataset['Memory2_type']=dataset['Memory2_type'].fillna('NA')
dataset['Gpu_version']=dataset['Gpu_version'].fillna('Unknown')
pd.set_option('display.max_columns',None)
# print(dataset.shape)
# print(dataset.isnull().sum())
print(dataset.duplicated())