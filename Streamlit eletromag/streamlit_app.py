import streamlit as st

# st.set_page_config(page_title="My Package App", page_icon="🧙🏼‍♂️")

# st.title("My Python Package Interface")

#-----------------Page setup-----------------

initial_page = st.Page(
    page="Pages/initial_Page.py",
    title= "Main informations",
    icon= ":material/home:",
    default=True,
)