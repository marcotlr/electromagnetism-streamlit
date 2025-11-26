import streamlit as st

# st.set_page_config(page_title="My Package App", page_icon="🧙🏼‍♂️")

# st.title("My Python Package Interface")

#-----------------Page setup-----------------

Documentation = st.Page(
    page="Pages/Documentation.py",
    title= "Main informations",
    icon= ":material/home:",
    default=True,
)

# about_page = st.Page(
#     page="Pages/About.py",
#     title= "About us",
#     icon= ":material/info:",
# )

coil_page = st.Page(
    page="Pages/Coil.py",
    title= "Coil",
    icon= ":material/bolt:",
)
IMG_PATH = "assets/Ilum.png"   # ajuste o caminho se estiver em outra pasta, ex: "assets/Ilum.png"

with st.sidebar:
    # imagem no topo da sidebar
    st.image(IMG_PATH, use_container_width=True)
    st.markdown("## SciMagNet")
    st.caption("Interface for the SciMag electromagnet library")

pg = st.navigation({
    "Info": [Documentation],
    "Package": [coil_page]})



pg.run()