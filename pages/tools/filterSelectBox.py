import streamlit as st

def apply_filter_select_box(string_to_filter, dataframe):
    filter_string = st.selectbox(f'Selecione a {string_to_filter}:', dataframe[string_to_filter].unique())
    filtered_df = dataframe[dataframe[string_to_filter] == filter_string]

    return filtered_df
