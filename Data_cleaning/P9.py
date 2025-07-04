import pandas as pd
import re
dataset=pd.read_csv(r'C:\Users\arind\Downloads\cleaned_laptopdata.csv')
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
# print(dataset.info)
# dataset=dataset.drop('Gpu',axis=1)
# print(dataset.info)
# dataset=dataset.to_csv(r'C:\Users\arind\Downloads\cleaned_laptopdata.csv')

# Weight
a=dataset['Weight'][0]
def weight(a):
    match=re.search(r'(\d+(\.\d+)?)(?=Kg)',a,re.IGNORECASE)
    return match[0] if match else None
dataset['Weight']=dataset['Weight'].apply(weight)
# print(dataset['Weight'].head(339))
dataset['Weight']=dataset['Weight'].replace('0.0002','0.2')
# print(dataset['Weight'].head(339))
# print(dataset.head(50))

dataset=dataset.to_csv(r'C:\Users\arind\Downloads\cleaned_laptopdata.csv')
print('saved successfully')