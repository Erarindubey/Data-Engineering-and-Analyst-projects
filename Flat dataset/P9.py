import pandas as pd
import re

# load
df=pd.read_csv(r'C:\Users\arind\Downloads\surat_cleaned2.csv')
pd.set_option('display.max_columns',None)

#                      Fixing  Status

# Inititalize
a=df['status'][0]

# retriving digits
def digits(a):
    index=len(a)
    for i in range(len(a)):
        if a[i].isdigit():
            index=i
            break;
    result=a[index:]
    return result

df['poss_by(year)']=df['status'].apply(digits)

# dict for digits
digit={
    24:2024, 26:2026, 27:2027,
    23:2023, 28:2028, 29:2029,
    30:2030, 31:2031, 32:2032,
    25:2025
}
digit_str={str(k): str(v) for k,v in digit.items()}
def digits2(a,digit):
   pattern='|'.join(re.escape(key) for key in digit.keys())
   return re.sub(pattern, lambda m: digit[m.group()],a)
df['poss_by(year)']=df['poss_by(year)'].apply(lambda x: digits2(str(x),digit_str))
# print(df.head(60))

# print(df['poss_by(year)'].iloc[60:110])

# dictionary to change months to numeric

date={
    'Jan': 'January',  'May':'May',   'Sep':'September',
     'Feb':'February',   'Jun':'June',   'Oct':'October',
    'Mar':'March',    'Jul':'July',   'Nov':'November',
    'Apr':'April',    'Aug':'August',    'Dec':'December'
}

# Retriving months

def month(a):
    match=re.search(r'Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec',a,re.IGNORECASE)
    return match[0] if match else "Instant"
df['Month']=df['status'].apply(month)
# print(df['Month'].head(50))

# Fixing String

def month2(a,date):
    pattern='|'.join(date.keys())
    return re.sub(pattern,lambda m: str(date[m.group()]),a)
df['Month']=df['Month'].apply(lambda x: month2(x,date))
# print(df['Month'].head(50))

df=df.to_csv(r'C:\Users\arind\Downloads\surat_cleaned2.csv')
print('Saved successfully')

