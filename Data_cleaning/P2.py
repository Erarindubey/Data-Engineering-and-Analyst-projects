import pandas as pd
import re
dataset=pd.read_csv(r"C:\Users\arind\Downloads\cleaned_laptopdata.csv")
pd.set_option('display.max_column',None)
# TypeName
# Dictionary to map digits to words
num_to_words = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
}

# Function to convert matched numbers to words
def convert_to_words(match):
    num1 = match.group(1)
    num2 = match.group(2)
    # Convert numbers to words using the dictionary
    word1 = ''.join(num_to_words[digit] for digit in num1)
    word2 = ''.join(num_to_words[digit] for digit in num2)
    return f"{word1} in {word2}"

# Apply the regex pattern to each column and row in the DataFrame
pattern = r'(\d+)\s*in\s*(\d+)'

def apply_conversion(row):
    for col in row.index:
        if isinstance(row[col], str):
            row[col] = re.sub(pattern, convert_to_words, row[col])
    return row

dataset = dataset.apply(apply_conversion, axis=1)

print(dataset["TypeName"])
# To Verify if column contains any integer
# def is_integer(value):
#     try:
#         int(value)
#         return True
#     except ValueError:
#         return False
# has_integers= dataset['TypeName'].apply(is_integer).any()
# if has_integers:
#     print(f"The column '{'TypeName'}' contains values that can be converted to integers.")
# else:
#     print(f"The column '{'TypeName'}' does not contain any values that can be converted to integers.")
dataset['TypeName']=dataset['TypeName'].astype('category')
print(dataset['TypeName'].dtypes)
dataset.to_csv(r"C:\Users\arind\Downloads\cleaned_laptopdata.csv",index=False)
print(r"changes saved to C:\Users\arind\Downloads\cleaned_laptopdata.csv")

