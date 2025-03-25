import streamlit as st

# Import modules
from utils import local_css
from pages.screens.home import home
from pages.screens.termsOfUse import change_state, initialize_session_state, terms_of_use
from pages.screens.calc import calc


print(st.session_state)
# Initialize session state variables
initialize_session_state()

print(st.session_state)

pages = {
    "Inicio": home,
    "Calc": calc,
}

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Calc Custos com Medicamentos",
        page_icon="💊",
        layout="centered",
        initial_sidebar_state="expanded",
    )
    # Load custom CSS
    local_css("style.css")

    # Check agreement before allowing access to other pages
    if not st.session_state.agreed:
        print(st.session_state)
        terms_of_use()
        print(st.session_state)
    else:
        # Sidebar navigation
        page = st.sidebar.radio("Navegação", list(pages.keys()), index=list(pages.keys()).index(st.session_state.current_page))
        change_state("Inicio", page)  # Save the current page in session state
        # Render the selected page
        pages[page]()

# Run the app
if __name__ == "__main__":
    main()