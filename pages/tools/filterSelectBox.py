import streamlit as st

def apply_filter_select_box(string_to_filter, dataframe):
    """Apply a filter to the dataframe based on the selected string
    args:
        string_to_filter: str: The column to filter
        dataframe: pd.DataFrame: The dataframe to filter
    return:
        """

    filter_strings = st.multiselect(f'Selecione as {string_to_filter}:', dataframe[string_to_filter].unique())
    filtered_df = dataframe[dataframe[string_to_filter].isin(filter_strings)]
    
    return filtered_df
