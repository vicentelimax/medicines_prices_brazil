import streamlit as st

# Import modules
from pages.tools.scrapData import get_data_url_from_anvisa
from pages.tools.processDataFrame import process_data_from_url
from pages.tools.filterSelectBox import apply_filter_select_box


def home():
    st.title('Calculadora de Custos com Medicametos para Doenças Inflamatórias')

    st.text("First Commit")

    # Cache the data loading function
    @st.cache_data
    def load_data():
        data = get_data_url_from_anvisa()
        return process_data_from_url(data)

    # Display a loading message while data is being loaded
    with st.spinner('Carregando dados de preços de medicamentos...'):
        df = load_data()
    st.success('Dados carregados com sucesso! Fonte: CMED, ANIVSA')

    # Filter by "SUBSTÂNCIA"
    filtered_df = apply_filter_select_box('SUBSTÂNCIA', df)

    # Filter by "LABORATÓRIO"
    filtered_df = apply_filter_select_box('LABORATÓRIO', filtered_df)

    # Filter by "APRESENTAÇÃO"
    filtered_df = apply_filter_select_box('APRESENTAÇÃO', filtered_df)

    # Filter by "ICMS"
    columns = df.loc[:, 'PF Sem Impostos':'PMC 22% ALC'].columns
    selected_column = st.selectbox('Selecione a Coluna:', columns)

    # Display the filtered data with the selected column
    filtered_df = filtered_df[['PRODUTO','APRESENTAÇÃO', selected_column]]

    st.write(filtered_df)

    st.write("Disponível em: https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/cmed/precos")
    


