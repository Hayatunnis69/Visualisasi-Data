import streamlit as st

st.title("Column")
st.write("**Kelompok 23**")
st.markdown("""
    - Amru Abdurrahman Azzam - 0110122322
    - Hayatunnisa - 0110222118
    - Nurul Maedatul Awaliah - 0110122222
 """)

("========================================================================================")

col1, col2, col3 = st.columns(3)

col1.write("Ini adalah kolom pertama")
col1.image("C:/Visdata/PRAKTIKUM 2/image/stoberi2.jpg")
col2.write("Ini adalah kolom kedua")
col2.image("C:/Visdata/PRAKTIKUM 2/image/lemon.jpg")
col3.write("Ini adalah kolom ketiga")
col3.image("C:/Visdata/PRAKTIKUM 2/image/stroberi.jpg")