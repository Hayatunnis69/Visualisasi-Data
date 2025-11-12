import streamlit as st
import time

st.title("Empty Containers")
st.write("Kelompok 23")
st.markdown("""
    - Amru Abdurrahman Azzam - 0110122322
    - Hayatunnisa - 0110222118
    - Nurul Maedatul Awaliah - 0110122222
 """)

("========================================================================================")

with st.empty():
    for seconds in range(5):
        st.write(f" {seconds} seconds have passed")
        time.sleep(1)
        st.write(" Time up!")