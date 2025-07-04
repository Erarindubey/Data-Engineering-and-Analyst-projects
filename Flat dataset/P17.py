import pandas as pd
from numpy.ma.extras import average

df=pd.read_csv(r'C:\Users\arind\Downloads\surat_cleaned3.csv')
pd.set_option('display.max_columns',None)
print(df.dtypes)