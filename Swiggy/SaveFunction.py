import pandas as pd
def save_to_csv(dataframe,filename,index=False):
    try:
        dataframe.to_csv(filename,index=index)
        print(f'Csv saved succesfully to {filename}')
    except Exception as e:
        print(f'An error occurred while saving the csv: {e}')
