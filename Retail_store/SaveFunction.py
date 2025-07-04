import pandas as pd
def save_to_csv(df,filename,index=False):
    try:
        df.to_csv(filename,index=index)
        print(f'csv file saved successfully to {filename}')
    except Exception as e:
        print(f'An error occured while saving the csv: {e}')
