import streamlit as st

# import data about tax and state.
from pages.tools.data_tax_state import load_tax_data

def load_tax_data_by_state():
    try:
        data_tax_by_state = load_tax_data()
        #data_tax_by_state = data_tax_by_state[0]
        return data_tax_by_state
    except:
        st.error("Erro ao carregar dados de ICMS por estado.")
        return None

def determing_is_generic_medicine(df_filtered_medicine):
    # RETIRAR A  STRING 'Genérico' DO JSON
    gerecic_string = 'Genérico'
    return df_filtered_medicine[df_filtered_medicine['TIPO DE PRODUTO (STATUS DO PRODUTO)'].str.contains(gerecic_string)].isnull().values.any()
 

def apply_state_filter(df_filtered_medicine):
    '''Apply a filter to select a state and return the ICMS rate for generic or other medicines
    return:
        string: ICMS rate column
    '''
    tax_data = load_tax_data_by_state()

    if not tax_data:
        st.error("Erro ao carregar dados de ICMS por estado.")
        return None
    
    # Debug: Print the loaded JSON data
    #st.write("Loaded tax data:", tax_data)
    states = []
    for item in tax_data:
        key = 'state'
        states.append(item[key])
    
    #states = [item[0] for item in dict_with_json_data]
    selected_state = st.selectbox('Selecione um Estado', states)
    generic_medicine = determing_is_generic_medicine(df_filtered_medicine)

    if generic_medicine:
        generic_tax_column = [item['generic_rate'] for item in tax_data if item['state'] == selected_state]
        st.write(f'Taxa de ICMS para medicamento genérico no estado de {selected_state}: {generic_tax_column[0]}')
        return generic_tax_column[0]
    else:
        other_tax_column = [item['other_rate'] for item in tax_data if item['state'] == selected_state]
        st.write(f'Taxa de ICMS para medicamento não genéricos no estado de {selected_state}: {other_tax_column[0]}')
        return other_tax_column[0]


