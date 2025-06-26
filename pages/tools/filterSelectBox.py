import streamlit as st
from pandas import DataFrame

def apply_filter_select_box(string_to_filter: str, dataframe: DataFrame) -> DataFrame:
    """Apply a filter to the dataframe based on the selected string
    args:
        string_to_filter: str: The column to filter
        dataframe: pd.DataFrame: The dataframe to filter
    return:
        """
    st.write(dataframe)
    filter_strings = st.multiselect(label=f'Selecione as {string_to_filter}: ', 
                                    options=dataframe[string_to_filter].unique())
    filtered_df = dataframe[dataframe[string_to_filter].isin(filter_strings)]
    
    return filtered_df
