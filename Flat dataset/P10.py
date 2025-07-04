import pandas as pd
df=pd.read_csv(r'C:\Users\arind\Downloads\surat_cleaned2.csv')
pd.set_option('display.max_columns',None)

# filtered_df=df[df['status'].str.contains('Ready',case=False)]
#
# filtered_df['poss_by(year)']=filtered_df['poss_by(year)'].fillna(2024)
# round(filtered_df['poss_by(year)'])

df['poss_by(year)']=df['poss_by(year)'].fillna(2024)

df['poss_by(year)']=df['poss_by(year)'].astype(int)

print(df.isnull().sum())

df=df.to_csv(r'C:\Users\arind\Downloads\surat_cleaned2.csv')
print('saved')
