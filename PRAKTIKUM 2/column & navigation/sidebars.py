import streamlit as st

st.title("Sidebar")
st.write("Kelompok 23")
st.markdown("""
    - Amru Abdurrahman Azzam - 0110122322
    - Hayatunnisa - 0110222118
    - Nurul Maedatul Awaliah - 0110122222
 """)

("========================================================================================")

st.sidebar.title("Sidebar")
st.sidebar.radio("Are You a New User", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0,10)