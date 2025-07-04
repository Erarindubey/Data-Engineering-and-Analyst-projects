import pandas as pd
df=pd.read_csv(r'C:\Users\arind\Downloads\swiggy_uncleaned.csv')
pd.set_option('display.max_columns',None)
# print(df.head(50).dtypes)

# df['food_type'] = df['food_type'].str.split(',')
#
# # Use explode to create separate rows for each cuisine
# df = df.explode('food_type')
#
# # Use one-hot encoding to create binary columns for each cuisine
# df = pd.get_dummies(df, columns=['food_type'], prefix='', prefix_sep='')
# print(df.head(50))

df['food_type'] = df['food_type'].str.split(',')
print(df.head(50))

df=df.to_csv(r'C:\Users\arind\Downloads\swiggy_uncleaned.csv')
print('saved')