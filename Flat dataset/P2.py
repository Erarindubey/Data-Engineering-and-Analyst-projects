import pandas as pd
df=pd.read_csv(r'C:\Users\arind\Downloads\surat_cleaned.csv')

# Check whether there is any null value

print(df.isnull().sum())

# Check the size of table

print(df.shape)

# Check data types they are stored in

print(df.dtypes)