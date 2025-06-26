import requests
import certifi
import pandas as pd

def process_data_from_url(xls_url):
    """Create a pandas DataFrame from an Excel file hosted on the CMED/ANVISA
    Also, set the header row and drop rows above it.
    args:
        xls_url: str
    return: 
        pandas DataFrame
    """
    print(xls_url)
    try:
        xls_response = requests.get(url=xls_url, verify=certifi.where())
        xls_response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"Request error: {e}")
        raise
    except requests.ConnectionError as e:
        print(f"Connection error: {e}")
        raise
    except requests.Timeout as e:
        print(f"Timeout error: {e}")
        raise

    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(xls_response.content)
    print(df.head(2))

    # Find the header row
    header_row_index = df[df.iloc[:, 0] == "SUBSTÂNCIA"].index[0]
    
    # Set the header row and drop rows above it
    df.columns = df.iloc[header_row_index]
    df = df.drop(range(header_row_index + 1)).reset_index(drop=True)
    return df
