import pandas as pd

# Read the CSV file using the provided path
dataset = pd.read_csv(r'C:\Users\arind\Downloads\laptopData.csv')
pd.set_option('display.max_columns',None)

# Define a function to check for "?" in a cell
def contains_question_mark(cell):
    return "?" in str(cell)

# Identify rows where any cell contains "?"
rows_with_question_mark = dataset.map(contains_question_mark).any(axis=1)

# Remove these rows from the dataset
dataset_cleaned = dataset[~rows_with_question_mark]

# Save the cleaned dataset to a new CSV file
dataset_cleaned.to_csv(r'C:\Users\arind\Downloads\cleaned_laptopdata.csv', index=False)
dataset=pd.read_csv(r'C:\Users\arind\Downloads\cleaned_laptopdata.csv')
# Display the cleaned dataset to check the changes
print(dataset.head(50))
