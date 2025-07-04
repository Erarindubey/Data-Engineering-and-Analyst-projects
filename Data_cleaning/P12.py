import pandas as pd
data=pd.read_csv(r"C:\Users\arind\Downloads\emp_data5626.csv",delimiter=';')
pd.set_option('display.max_columns',None)

print(data.dtypes)
data["hire_date"]=pd.to_datetime(data['hire_date'])
print(data.dtypes)
filtered_data=data[data['hire_date']<pd.to_datetime('1990-12-31')]
print(filtered_data)