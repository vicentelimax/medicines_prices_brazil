import streamlit as st

# Import modules
from pages.tools.scrapData import get_data_url_from_anvisa
from pages.tools.processDataFrame import process_data_from_url
from pages.tools.filterSelectBox import apply_filter_select_box
from pages.tools.filter_state import apply_state_filter
from pages.tools.factor_price import add_factor_price

def home():
    st.header('Consulta de preços de Medicamentos CMED/ANVISA')

    # Cache the data loading function
    @st.cache_data
    def load_data():
        data = get_data_url_from_anvisa()
        return process_data_from_url(data)

    # Display a loading message while data is being loaded
    with st.spinner('Carregando dados de preços de medicamentos...'):
        try:
            df = load_data()
        except:
            st.error('Erro ao carregar dados de preços de medicamentos da ANVISA. Tente novamente mais tarde.')
            return
    st.success('Dados carregados com sucesso! Fonte: CMED, ANIVSA')

    # Filter by "SUBSTÂNCIA"
    filtered_df = apply_filter_select_box('SUBSTÂNCIA', df)

    # Filter by "LABORATÓRIO"
    filtered_df = apply_filter_select_box('LABORATÓRIO', filtered_df)

    # Filter by "APRESENTAÇÃO"
    filtered_df = apply_filter_select_box('APRESENTAÇÃO', filtered_df)

    # Add a factor to the price
    filtered_df = add_factor_price(filtered_df)

    # Filter by State/ICMS
    column_to_filter_tax_state = apply_state_filter(filtered_df)

    # Display the filtered data with the selected column
    filtered_df = filtered_df[['PRODUTO','APRESENTAÇÃO', column_to_filter_tax_state, 'fator']]
 

    st.write(filtered_df.reset_index(drop=True))

    st.write("Disponível em: https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/cmed/precos")

    if st.button("Ir para Calculadora"):
        st.switch_page("./calc.py")
    


