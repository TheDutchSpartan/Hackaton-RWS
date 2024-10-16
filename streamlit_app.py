import streamlit as st

st.sidebar.title('Blog categorieën')
blog_post = st.sidebar.selectbox(
    'Selecteer een onderwerp',
    ('Introductie', 'Aannames', 'Informatie terrein', 'Energiebehoefte', 'Conclusie/Aanbevelingen'))
