import streamlit as st
import pandas as pd
import numpy as np

st.title("Map View")
st.write("**Kelompok 23**")
st.markdown("""
    - Amru Abdurrahman Azzam - 0110122322
    - Hayatunnisa - 0110222118
    - Nurul Maedatul Awaliah - 0110122222
 """)

("========================================================================================")

df = pd.DataFrame(
    np.random.randn(50, 2)/[10, 10] + [15.458, 75.0078],
    columns=["latitude", "longitude"]
)
st.map(df)