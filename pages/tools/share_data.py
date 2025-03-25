import streamlit as st
from pages.tools.scrapData import get_data_url_from_anvisa
from pages.tools.processDataFrame import process_data_from_url

# Cache the data loading function
@st.cache_data
def load_data():
    data = get_data_url_from_anvisa()
    return process_data_from_url(data)

# def transport_filtered_dataframes_index(filtered_dataframe):
#     """Transport the filtered dataframe to another page"""
#     # Store the filtered DataFrame in session state
#     st.session_state.filtered_dataframe = filtered_dataframe