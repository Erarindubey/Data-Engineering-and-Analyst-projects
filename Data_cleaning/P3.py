# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import re
# dataset=pd.read_csv(r'C:\Users\arind\Downloads\cleaned_laptopdata.csv')
# dataset=pd.set_option('display.max_columns',None)
# print((dataset.head(1)))
# dataset.info()
# print(dataset.isnull().sum())
# print(dataset.shape[0])
# print((dataset.isnull().sum()/dataset.shape[0])*100)


# y=dataset[~dataset.apply(lambda col: col.astype(str).str.contains(r'\?')).any(axis=1)]

# Inches
# d=pd.to_numeric(dataset['Inches'],errors='coerce')
# print(d.dtype)
# dataset.info()

# Screen Resolution
# x=dataset['ScreenResolution'][0]
# index=len(x)
# for k in range(len(x)):
#     if x[k].isdigit():
#         index=k
#         break
# result69 =x[:index]
# print(result69)
# def screen(x):
#     index = len(x)
#     for k in range(len(x)):
#         if x[k].isdigit():
#             index = k
#             break
#     result69 = x[:index]
#     return result69
# def resolution(x):
#     index = len(x)
#     for k in range(len(x)):
#         if x[k].isdigit():
#             index = k
#             break
#     result70 = x[index:]
#     return result70
# dataset["screem"]=dataset["ScreenResolution"].apply(screen)
# dataset["resolution"]=dataset["ScreenResolution"].apply(resolution)
# # print(dataset["resolution"])
# print(dataset.head(3))
# # TypeName
# dataset['TypeName']=dataset['TypeName'].astype('category')
# print(dataset['TypeName'].dtype)
# Ram
# x=dataset['Ram'][0]
# def Ram(x):
#     index=len(x)
#     for k in range(len(x)):
#         if x[k]=="GB":
#             index=k
#             break
#         result69=x[:(index-2)]
#         return result69
# dataset["Ram"]=dataset["Ram"].apply(Ram)
# y=dataset['Ram'].astype('int64')
# dataset['Ram']=y
# dataset["Ram"]=dataset["Ram"]*1000
# print(dataset["Ram"].info)

# Memory

# l=dataset["Memory"]
# def memory_space1(l):
#     match=re.search(r'(\d+)(?=GB)',l)
#     if match:
#        return match.group(1)
#     match2=re.search(r'(\d+)(?=TB)',l)
#     if match2:
#        return int(match2.group(1))*1024
#     return None
# dataset["Memory_space1"]=dataset["Memory"].apply(memory_space1)
# dataset["Memroy_space1"]=dataset["Memory_space1"].fillna(0)
# dataset["Memory_space1"]=dataset["Memory_space1"].astype(int)
# def memory_type1(l):
#     match =re.search(r'(?:\d+GB|\d+TB)\s*(\w+\s*\w*)(?=\s*\+|\s*$)',l)
#     return match.group(1) if match else None
# dataset["Memory_type1"]=dataset['Memory'].apply(memory_type1)
# # print(dataset[dataset.isnull().any(axis=1)])
# # print(dataset.isnull().sum())
# # print(dataset["Memory_space1"].isnull().sum())
# print(dataset["Memory","Memory_space1","Memory_type1"])

