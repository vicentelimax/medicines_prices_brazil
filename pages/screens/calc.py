import streamlit as st

# Import modules
from pages.tools.share_data import transport_filtered_dataframes_index

def calc():

    st.header('Calculadora de Custos com Medicamentos')

    # Retrieve the filtered DataFrame from session state
    if "filtered_dataframe" in st.session_state:
        filtered_data = st.session_state.filtered_dataframe
        
        st.write("Medicamentos importados:")
        st.write(filtered_data)
    else:
        st.warning("No filtered data found. Please go to Page 1 and filter the data first.")

    st.text("Informações de tratamento.")

    # Processamento do DataFrame
    filtered_data.loc[:, 'concatened'] = filtered_data['PRODUTO'] + ' - ' + filtered_data['APRESENTAÇÃO']
    price_column = f"{filtered_data.columns[2]}"
    filtered_data[price_column] = filtered_data[price_column].astype(float)
    filtered_data.loc[:, 'ajusted_value'] = filtered_data[price_column] / filtered_data['fator']

    option = st.selectbox(
        label="Selecione o Medicamento da lista acima",
        options=filtered_data['concatened'].unique()
    )

    filtered_option = filtered_data[filtered_data['concatened'] == option]

    st.write(filtered_option)

    

    

    

    