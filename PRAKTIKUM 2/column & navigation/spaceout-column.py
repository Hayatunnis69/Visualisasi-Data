import streamlit as st

st.title("Spaced_Output Colomns")
st.write("Kelompok 23")
st.markdown("""
    - Amru Abdurrahman Azzam - 0110122322
    - Hayatunnisa - 0110222118
    - Nurul Maedatul Awaliah - 0110122222
 """)

("========================================================================================")

from PIL import Image
img = Image.open("C:/Visdata/PRAKTIKUM 2/image/stroberi.jpg")

for _ in range(2):

    cols = st.columns((3, 1, 2, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)