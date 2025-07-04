import pandas as pd
import re
dataset=pd.read_csv(r'C:\Users\arind\Downloads\cleaned_laptopdata.csv')
pd.set_option('display.max_columns',None)
# dataset62=dataset.drop('Cpu',axis=1)
# dataset62=dataset62.to_csv(r'C:\Users\arind\Downloads\cleaned_laptopdata.csv')
# print(dataset.dtypes)
# Ram

x=dataset['Ram']
def Ram(x):
    index=len(x)
    for k in range(len(x)):
        if x[k]=="GB":
            index=k
            break
        result69=x[:(index-2)]
        return result69
dataset["Ram"]=dataset["Ram"].apply(Ram)
y=dataset['Ram'].astype('int64')
dataset['Ram']=y
dataset["Ram"]=dataset["Ram"]*1000
print(dataset["Ram"].info)
dataset12=dataset.to_csv(r'C:\Users\arind\Downloads\cleaned_laptopdata.csv')


print(dataset.info)