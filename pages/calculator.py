import streamlit as st
import locale

# Import modules
# from pages.tools.share_data import transport_dfframes_index
from pages.tools.factor_price import add_factor_price
from pages.tools.filter_state import apply_state_filter

# Configura o locale para o padrão brasileiro
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

def calc():

    st.header('Calculadora de Custos com Medicamentos')

    # Retrieve the filtered DataFrame from session state
    if "df" in st.session_state:
        df = st.session_state.df
    else:
        st.warning("Dados não carregados. Por favor, volte para a página de Início para carregar os dados.\nCaso o erro persista, tente novamente mais tarde.")

    st.subheader("Informações de tratamento")


    # Processamento do DataFrame
    df.loc[:, 'concatened'] = df['PRODUTO'] + ' - ' + df['APRESENTAÇÃO'] + ' - ' + df['LABORATÓRIO']
    # price_column = f"{df.columns[2]}"
    # df[price_column] = df[price_column].astype(float)
    # df.loc[:, 'ajusted_value'] = df[price_column] / df['fator']

    option = st.selectbox(
        label="Selecione o Medicamento da lista acima",
        options=df['concatened'].unique()
    )

    filtered_by_option = df[df['concatened'] == option]

    # Add a factor to the price
    filtered_df = add_factor_price(filtered_by_option)

    # Filter by State/ICMS
    column_to_filter_tax_state = apply_state_filter(filtered_df)

    # I need to transform now the column to float to show as float number too
    filtered_df.loc[:, column_to_filter_tax_state] = filtered_df[column_to_filter_tax_state].astype(float)

    # Display the filtered data with the selected column
    filtered_df = filtered_df[['PRODUTO','APRESENTAÇÃO', column_to_filter_tax_state, 'fator']]

    # This position is important because there are fewer bytes to consume
    filtered_df.loc[:, 'VALOR UNITÁRIO'] = round(filtered_df[column_to_filter_tax_state] / filtered_df['fator'], 2)

    st.write(filtered_df.reset_index(drop=True))

    unitary_value = filtered_df['VALOR UNITÁRIO'].values[0].astype(float)
    st.write(f"Valor Unitário: R$ {unitary_value:.2f}")

    st.write("Disponível em: https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/cmed/precos")

    col1, col2 = st.columns(2, vertical_alignment='center')
    with col1:
        # Doses
        doses = st.number_input(
            key="doses",
            label="Número de Unidades Unitárias por Dose.",
            value=1,
            min_value=1,
            max_value=1000
        )
    with col2:
        # Frequency
        frequency = st.number_input(
            key="frequency",
            label="Frequência de Administração em dias.",
            value=30,
            min_value=1,
            max_value=365
        )
    
    col1, col2 = st.columns(2, vertical_alignment='center')
    st.write("Duração total do Tratamento.")
    with col1:
        options = ["Dias", "Meses", "Anos"]
        selection = st.segmented_control(
            "Tempo", options, selection_mode="single",
            default="Dias"
        )
        st.markdown(f"Your selected options: {selection}.")
        
    with col2:
        # Duration
        duration = st.number_input(
            key="duration",
            label="Duração total do Tratamento em dias",
            value=365,
            min_value=1,
            max_value=365
        )



    def show_brazil_format_number(number):
        # Configura o locale para o padrão brasileiro
        locale.setlocale(locale.LC_ALL, "pt_BR")
        # Formata o número
        return locale.format_string("%.2f", number, grouping=True)
    
    # Initialize the basket
    if "basket" not in st.session_state:
        st.session_state.basket = []

    if "option_text" not in st.session_state:
        st.session_state.option_text = [] # Ta confuso

    # Add item to the basket
    def add_item(value):
        if len(st.session_state.basket) < 4:
            st.session_state.basket.append(value)
            st.session_state.option_text.append(filtered_by_option['concatened'].unique())
        else:
            st.warning("Você pode comparar até 3 medicamentos por vez")
    
    if st.button("Adicionar ao Carrinho"):
        total_cost = round(unitary_value * doses * (int(duration / frequency)), 2)
        add_item(total_cost)
        st.success("Item adicionado ao carrinho com sucesso!")

    # Show current item
    #st.metric(label="Custo Calculado", value=f"R$ {show_brazil_format_number(round(unitary_value * doses * (int(duration / frequency)), 2))}")

    # Show the basket
    st.write("Cesta de comparação: ")
    if st.session_state.basket:
        col1, col2, col3 = st.columns(3)

        for i, value in enumerate(st.session_state.basket):
            with eval(f"col{i+1}"):
                st.container().write(f"Item: {st.session_state.option_text[0]}: ") #### Ver isso
                st.metric(label=f"Item {i+1}", value=f"R$ {show_brazil_format_number(value)}")
                st.divider()

    else:
        st.info("Nenhum item adicionado ao carrinho")

    def clear_basket():
        st.session_state.basket = []
        st.success("Cesta de comparação limpa com sucesso!")
        st.query_params.clear()
        st.rerun()

    st.button("Limpar Cesta", on_click=clear_basket)
    if 'basket' in st.session_state and len(st.session_state.basket) == 0:
        st.success("Cesta de comparação limpa com sucesso!")


    

    

    

    