import pandas as pd
import re
df=pd.read_csv(r'C:\Users\arind\Downloads\surat_cleaned2.csv')
print(df.isnull().sum())
print(df.head(50))