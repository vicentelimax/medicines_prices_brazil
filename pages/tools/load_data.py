import streamlit as st
from pages.tools.scrapData import get_data_url_from_anvisa
from pages.tools.processDataFrame import process_data_from_url

# Cache the data loading function
@st.cache_data
def load_data():
    data = get_data_url_from_anvisa()
    print(data)
    return process_data_from_url(data)

