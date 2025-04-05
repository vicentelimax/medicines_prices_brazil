import streamlit as st

# Import modules
from utils import local_css
from pages.termsOfUse import initialize_session_state, terms_of_use
import pages.home as home
import pages.calculator as calc

# Fast debbuging. DELETE LATER
print(st.session_state)

# Initialize session state variables
initialize_session_state()

pages = {
    "Inicio": home.home,
    "Calc": calc.calc,
}

def navigate_too(page_name):
    """ Change the current page in session state.
    """
    st.session_state.current_page = page_name

    # Fast debbuging. DELETE LATER
    print(f"Page changed to: {st.session_state.current_page}")


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
        terms_of_use()
    else:

        # Sidebar navigation
        page = st.sidebar.radio(
            "Navegação", 
            list(pages.keys()), 
            index=list(pages.keys()).index(st.session_state.current_page),
            on_change=lambda: navigate_too(page),
            )
        
        # Render the selected page
        pages[st.session_state.current_page]()

# Run the app
if __name__ == "__main__":
    main()