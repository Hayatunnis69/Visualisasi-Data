import streamlit as st

st.title("Column w Padding")
st.write("Kelompok 23")
st.markdown("""
    - Amru Abdurrahman Azzam - 0110122322
    - Hayatunnisa - 0110222118
    - Nurul Maedatul Awaliah - 0110122222
 """)

("========================================================================================")

from PIL import Image
img = Image.open("C:/Visdata/PRAKTIKUM 2/image/stoberi2.jpg")

col1, padding, col2 = st.columns((10,2,10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)