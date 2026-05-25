import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(layout="wide")

st.markdown(
    """
    <h1 style='
        font-family: Arial;
        color: #ff4b4b;
        font-size: 50px;
        font-family: "Poppins", sans-serif;
        font-weight: 700;
        text-align: center;
    '>
    Customer Purchase Behaviour Data Analysis: Dashboard
    </h1>
    """,
    unsafe_allow_html=True
)

options = st.selectbox(
    "Choose a Chart to view:",
    ['Distribution Of Each Category Items: Gender wise',
     'Maximum - Minimum Frequency Of Purchase: Gender wise',
     'Overall Frequency of Purchase Distribution: Gender wise',
     'Distribution of Each Category Items: Gender and Season wise',
     'Average Amount (USD) Spent On Each Category: Gender wise',
     'Probability Distribution For Each Category Count']
)

if options == "Distribution Of Each Category Items: Gender wise":
    tableau_url = """
    https://public.tableau.com/views/Book1category_items/Dashboard3?:showVizHome=no
    """
    tableau_iframe = f"""
    <div class='tableauPlaceholder'>
        <iframe
            src="{tableau_url}"
            width="100%"
            height="900"
            frameborder="0"
            allowfullscreen>
        </iframe>
    </div>
    """
    components.html(tableau_iframe, height=900)

elif options == "Maximum - Minimum Frequency Of Purchase: Gender wise":
    tableau_url = """
    https://public.tableau.com/views/Book1category_items/Sheet8?:showVizHome=no
    """
    tableau_iframe = f"""
    <div class='tableauPlaceholder'>
        <iframe
            src="{tableau_url}"
            width="100%"
            height="900"
            frameborder="0"
            allowfullscreen>
        </iframe>
    </div>
    """
    components.html(tableau_iframe, height=900)

elif options == "Overall Frequency of Purchase Distribution: Gender wise":
    tableau_url = """
    https://public.tableau.com/views/Book1category_items/Dashboard1?:showVizHome=no
    """
    tableau_iframe = f"""
    <div class='tableauPlaceholder'>
        <iframe
            src="{tableau_url}"
            width="100%"
            height="900"
            frameborder="0"
            allowfullscreen>
        </iframe>
    </div>
    """
    components.html(tableau_iframe, height=900)

elif options == "Distribution of Each Category Items: Gender and Season wise":
    tableau_url = """
    https://public.tableau.com/views/Book1category_items/Sheet12?:showVizHome=no
    """
    tableau_iframe = f"""
    <div class='tableauPlaceholder'>
        <iframe
            src="{tableau_url}"
            width="100%"
            height="900"
            frameborder="0"
            allowfullscreen>
        </iframe>
    </div>
    """
    components.html(tableau_iframe, height=900)

elif options == "Average Amount (USD) Spent On Each Category: Gender wise":
    tableau_url = """
    https://public.tableau.com/views/Book1category_items/Sheet13?:showVizHome=no&:embed=true
    """

    tableau_iframe = f"""
    <div class='tableauPlaceholder'>
        <iframe
            src="{tableau_url}"
            width="100%"
            height="1200"
            frameborder="0"
            allowfullscreen>
        </iframe>
    </div>
    """
    components.html(tableau_iframe, height=900)

elif options == "Probability Distribution For Each Category Count":
    tableau_url = """
    https://public.tableau.com/views/Book1category_items/Dashboard2?:showVizHome=no
    """
    tableau_iframe = f"""
    <div class='tableauPlaceholder'>
        <iframe
            src="{tableau_url}"
            width="100%"
            height="900"
            frameborder="0"
            allowfullscreen>
        </iframe>
    </div>
    """
    components.html(tableau_iframe, height=900)