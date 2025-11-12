import streamlit as st

st.title("Grid")
st.write("Kelompok 23")
st.markdown("""
    - Amru Abdurrahman Azzam - 0110122322
    - Hayatunnisa - 0110222118
    - Nurul Maedatul Awaliah - 0110122222
 """)

("========================================================================================")

from PIL import Image
img = Image.open("C:/Visdata/PRAKTIKUM 2/image/libit.jpg")

for a in range(4):
    cols = st.columns((1, 1, 1, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)