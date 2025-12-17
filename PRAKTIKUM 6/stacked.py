#import library
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


st.title("Praktikum 6 Visualisasi Data")
st.write("**Kelompok 23**")
st.markdown("""
    - Amru Abdurrahman Azzam - 0110122322
    - Hayatunnisa - 0110222118
    - Nurul Maedatul Awaliah - 0110122222
 """)


#dataset
stores = ['Store A', 'Store B', 'Store C']
male = [150, 200, 180]
female = [120, 230, 170]


#data transaksi penjualan
stores = ['Store A', 'Store B', 'Store C']
product_a = [200, 250, 300]
product_b = [150, 300, 200]

#data quarter
q1_male = [150, 180, 160]
q1_female = [140, 200, 180]
q2_male = [170, 190, 175]
q2_female = [130, 210, 160]

#Garfik stacked version bar chart
st.subheader("1. Stacked Vertikal Bar Chart")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, male, label = 'Male', color = 'lightblue')
ax.bar(x, female, bottom=male, label = 'Female', color = 'Pink')

ax.set_title('Population by Gender and Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)


("-----------------------------------------------------------------")


#Grafik stacked vertikal bar chart
st.subheader("2. Stacked Vertikal Bar Chart dengan Matplotlib")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, product_a, label = 'Product A', color = 'maroon')
ax.bar(x, product_b, bottom=male, label = 'Product B', color = 'orange')

ax.set_title('Sales Transaction by Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)

("-----------------------------------------------------------------")


# Grafik kustomisasi stacked vertikal bar chart 
st.subheader("3. Kustomisasi Stacked Vertikal Bar Chart")

for i in range(len(x)):
    plt.text(x[i], product_a[i]/2, str(product_a[i]), ha = 'center', color = 'white')
    plt.text(x[i], product_a[i] + product_b[i]/2, str(product_b[i]), ha = 'center', color = 'black')
st.pyplot(fig)

("-----------------------------------------------------------------")


#Grafik Multiple Stacked Vertical Bar Chart
st.subheader("4. Multiple Stacked Vertikal Bar Chart")

fig, ax = plt.subplots()
width = 0.4
x = np.arange(len(stores))

ax.bar(x - width/2, q1_male, label = 'Q1 Male', color = 'lightblue', width=width)
ax.bar(x - width/2, q1_female, bottom=q1_male, label = 'Q1 Female', color = 'chocolate', width=width)

ax.bar(x - width/2, q2_male, label = 'Q2 Male', color = 'green', width=width)
ax.bar(x - width/2, q2_female, bottom=q2_male, label = 'Q2 Female', color = 'yellow', width=width)


ax.set_title('Population by Gender and Store (Multiple Quarter)')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)