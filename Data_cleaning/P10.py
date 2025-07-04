import pandas as pd
from sqlalchemy import create_engine
dataset=pd.read_csv(r'C:\Users\arind\Downloads\cleaned_laptopdata.csv')
pd.set_option('display.max_columns',None)
# print(dataset.head(50))
engine=create_engine(r'mysql+pymysql://root:Arin5626@localhost/employees')
dataset2=dataset.to_sql(r'cleaned_laptopdata.sql',engine)
print('Saved successfully')