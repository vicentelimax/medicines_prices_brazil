import requests
import pandas as pd

def process_data_from_url(xls_url):
    """Create a pandas DataFrame from an Excel file hosted on the CMED/ANVISA
    Also, set the header row and drop rows above it.
    args:
        xls_url: str
    return: 
        pandas DataFrame
    """
    xls_response = requests.get(xls_url)
    
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(xls_response.content)

    # Find the header row
    header_row_index = df[df.iloc[:, 0] == "SUBSTÂNCIA"].index[0]
    
    # Set the header row and drop rows above it
    df.columns = df.iloc[header_row_index]
    df = df.drop(range(header_row_index + 1)).reset_index(drop=True)
    return df
