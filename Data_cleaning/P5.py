import pandas as pd
import re
dataset=pd.read_csv(r"C:\Users\arind\Downloads\cleaned_laptopdata.csv")
pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)
# CPU
a=dataset['Cpu']

# step 1 remove cpu_company from cpu

def cpu_company(a):
    if pd.isna(a):
        return "Unknown"
    match=re.search(r'Intel|AMD|Samsung',a,re.IGNORECASE)
    return match.group(0) if match else "Unknown"
dataset['Cpu_company']=dataset['Cpu'].apply(cpu_company)
# print(dataset['Cpu_company'].head(50))

# Step 2 remove Cpu series from Cpu

def cpu_series(a):
    if pd.isna(a):
        return " Unknown"
    match = re.search(r'core i\d+|ryzen|Atom|Atom x\d+|Fx|Celeron \b|Pentium|Xeon E\d+|A\d+|E-series|core m m\d+|Cortex',a,re.IGNORECASE)
    match=match[0] if match else "Unknown"
    return match
dataset["Series"]=dataset['Cpu'].apply(cpu_series)
# print(dataset['Series'].head(1270))

#Step 3 remove cores from cpu

def cpu_cores(a):
    if pd.isna(a):
        return 'Unknown'
    match=re.search(r'Quad\s*core|dual\score|Octa\score',a,re.IGNORECASE)
    match=match[0] if match else 'Unknown'
    return match
dataset['Cores']=dataset['Cpu'].apply(cpu_cores)
# print(dataset['Cores'].head(1000))

#Step 4 remove cpuversion from cpu

def cpu_version(a):
    if pd.isna(a):
        return 'Unknown'
    version = re.findall(r'\w*\d+\w*\d+\w*',a,re.IGNORECASE)
    version = version[0] if version else ("Unknown")
    return version
dataset['Cpu_Version']=dataset['Cpu'].apply(cpu_version)
# print(dataset['Cpu_Version'].head(50))

#Step5 remove speed from cpu

def cpu_speed(a):
    if pd.isna(a):
        return "Unknown"
    match=re.search(r'\d+\.\d+(?=\w*)',a,re.IGNORECASE)
    if match:
        return match[0]
    else:
        match=re.search(r'\d+(?=Ghz)',a,re.IGNORECASE)
        return match[0] if match else ("Unknown")
    return match
dataset['Cpu_Clock_speed(Ghz)']=dataset['Cpu'].apply(cpu_speed)
dataset['Cpu_Clock_speed(Ghz)']=dataset['Cpu_Clock_speed(Ghz)'].astype(float)
# print(dataset['Cpu_Clock_speed(Ghz)'].head(100))
print(dataset.info)
dataset=dataset.to_csv(r'C:\Users\arind\Downloads\cleaned_laptopdata.csv')