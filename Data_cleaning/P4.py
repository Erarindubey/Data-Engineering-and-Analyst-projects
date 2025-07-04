import pandas as pd
import re
# ScreenResolution
dataset=pd.read_csv(r"C:\Users\arind\Downloads\cleaned_laptopdata.csv")
pd.set_option('display.max_column',None)
a=dataset['ScreenResolution'][0]
# Step 1 remove screen type/display type from screenresolution

def Panel_type(a):
    if pd.isna(a):
        return 'Unknown'
    cleaned_text = re.sub(r'\d+x\d+|\d+K|\d+', '', a)  # fixed regex
    words = re.findall(r'\b[a-zA-Z]+\b', cleaned_text)  # or use \b[\w]+\b
    if not words:
        return 'Unknown'
    return ' '.join(words)
dataset["Display_type"] = dataset['ScreenResolution'].apply(Panel_type)

# Step 2 remove display height from SR

def height(a):
    match=re.search(r'(\d+)(?=x)',a)
    return match.group(1) if match else None
dataset["Height"]=dataset["ScreenResolution"].apply(height).astype(int)

# Step 3 remove display width from SR

def width(a):
    match=re.search(r'x(\d+)',a)
    return match.group(1) if match else None
dataset["Width"]=dataset["ScreenResolution"].apply(width).astype(int)

# Step 4 check touchscreen

def touchscreen(a):
    if pd.isna(a):
        return False
    match=re.search(r'(touchscreen)',a,re.IGNORECASE)
    return True if match else False
dataset["Touchscreen"]=dataset["ScreenResolution"].apply(touchscreen)

# Step 5 check 4K ULTRAHD

def ultrahd(a):
    if pd.isna(a):
        return False
    match=re.search(r'(4k|ultrahd|UHD)',a,re.IGNORECASE)
    return True if match else False
dataset["4k_UHD"]=dataset["ScreenResolution"].apply(ultrahd)
# print(dataset['4k_UHD'].head(200))

# Step 6 drop SR

dataset=dataset.drop("ScreenResolution",axis=1)

# Verify

print(dataset.info)

# Step 7 Save changes

dataset64=dataset.to_csv(r"C:\Users\arind\Downloads\cleaned_laptopdata.csv")

print(" dataset saved to location ",dataset64)