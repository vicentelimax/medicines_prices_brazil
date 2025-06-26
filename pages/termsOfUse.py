import streamlit as st

def initialize_session_state():
    """
    Initialize the session state variables.
    This function checks if certain keys are present in the Streamlit session state.
    If the keys are not present, it initializes them with default values.
    - "agreed": A boolean indicating whether the user has agreed to the terms of use.
      Default value is False.
    - "current_page": A string indicating the current page the user is on.
      Default value is "Termos de Uso".
    """
    if "agreed" not in st.session_state:
        st.session_state.agreed = False
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Termos de Uso"

#@st.dialog("Termos e Consentimento")
def change_state(state_key, value):
    """Change the state of the app"""
    st.session_state[state_key] = value

def terms_of_use():
    """
    Render the Terms of Use page.
    This page is shown until the user agrees to the terms of use.
    """
    st.markdown(
        """
        <h1 style="color: white;">
            <span style="color: orange;">Bem vindo</span> ao Aplicativo de Análise de Custos com Medicamentos
        </h1>
        <hr style="border: 3px 1px solid gray;">
        """,
        unsafe_allow_html=True,
    )

    st.title("Termos de Uso e Consentimento")
    st.write(f"Leia atentamente os termos de uso do Aplicativo.")
    st.markdown("""
        <div class="terms-of-use">
            Este aplicativo utiliza dados públicos sobre preços de medicamentos disponibilizados pela CMED/ANVISA. O objetivo é oferecer uma ferramenta simples e intuitiva para que você possa explorar e analisar esses dados de forma mais acessível. É importante ressaltar que 
            os dados utilizados podem não refletir a realidade do mercado em tempo real e podem não estar atualizados. As informações apresentadas 
            neste aplicativo são fornecidas apenas para fins informativos e não devem ser utilizadas como base para decisões médicas ou financeiras.
            <br>Ao utilizar este aplicativo, você concorda que:<br>
                - Compreende a natureza pública dos dados utilizados.<br>
                - Reconhece que os dados podem estar sujeitos a alterações e podem não ser completamente precisos.<br>
                - Isenta os desenvolvedores do aplicativo de qualquer responsabilidade por decisões tomadas com base nas informações aqui apresentadas.<br> 
        </div>
    """, unsafe_allow_html=True)


        # Logic to show the buttons and changes the session state variables
        # if st.session_state.show_agree_buttons:
        #     col1, col2 = st.columns(2, gap='small', vertical_alignment='top')
        #     with col1:
        #         if st.button("Concordo", type='secondary'):
        #             st.session_state.show_agree_buttons = False
        #             st.session_state.agreed = True
        #             st.session_state.current_page = "Inicio"
        #             st.rerun()
        #             #st.query_params.clear() # Reload the app
                    
        #     with col2:
        #         if st.button("Não Concordo", type='secondary'):
        #             st.session_state.show_agree_buttons = False
        #             st.session_state.agreed = False
        #             st.query_params.clear() # Reload the app
        #             st.rerun()

        # Botões para aceitar ou recusar os termos
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Concordo"):
            st.session_state.agreed = True
            st.session_state.current_page = "Inicio"  # Define a página inicial após aceitar os termos
            st.query_params.clear()  # Limpa os parâmetros da URL
            st.rerun()  # Recarrega o app para aplicar a mudança
    with col2:
        if st.button("Não Concordo"):
            st.session_state.agreed = False
            st.error("Você deve aceitar os termos para usar o aplicativo.")

    # else:
    #     if not st.session_state.agreed:
    #         st.error("O aplicativo foi encerrado!")
    #         st.markdown("[Clique aqui para reiniciar o aplicativo](./)")
    #     elif st.button("Iniciar App"):
    #         st.session_state.agreed = True