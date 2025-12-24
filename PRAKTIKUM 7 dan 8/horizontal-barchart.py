import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#Judul
st.title("Praktikum 7 Visualisasi Data")
st.subheader("Horizontal Bar Chart  Stacked Bar Chart")
st.write("**Kelompok 23**")
st.markdown("""
    - Amru Abdurrahman Azzam - 0110122322
    - Hayatunnisa - 0110222118
    - Nurul Maedatul Awaliah - 0110122222
 """)


#dataset
brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
sales_2023 = [350, 420, 300, 280]
sales_2024 = [380, 450, 320, 300]

#atur y
y = np.arange(len(brands))
bar_width = 0.4

#filter kategori
kategori = st.selectbox(
    "Pilih Kategori Visualisasi",
    ['Basic Bar Chart', 'Kustomisasi Grafik', 'Multiple Chart']
)


#basic bar chart
if kategori == "Basic Bar Chart":
    st.subheader("Horizontal Bar Chart Sederhana")

    fig1, ax1 = plt.subplots()

    #grafik batang horizontal
    ax1.set_yticks(y)
    ax1.set_yticklabels(brands)
    ax1.set_title('Horizontal Bar Chart')
    ax1.set_xlabel('Jumlah Penjualan')
    ax1.set_ylabel('Merk')
    ax1.barh(y, sales_2023, color='pink')
    
    st.pyplot(fig1)

    #grafik stacked
    st.subheader("Stacked Horizontal Bar Chart Sederhana")

    fig2, ax2 = plt.subplots()

    ax2.set_yticks(y)
    ax2.set_yticklabels(brands)
    ax2.set_title('Stacked Horizontal Bar Chart - 2023')
    ax2.set_xlabel('Jumlah Penjualan')
    ax2.set_ylabel('Merk')
    ax2.barh(y, sales_2023, color='yellow', label = '2023')
    ax2.barh(y, sales_2024, color='lightgreen', label = '2024', left=sales_2023)
    ax2.legend()

    st.pyplot(fig2)


#customisasi
elif kategori == "Kustomisasi Grafik":
    st.subheader('Kustomisasi Horizontal Bar Chart')

    fig3, ax3 = plt.subplots()

    ax3.set_yticks(y)
    ax3.set_yticklabels(brands)
    ax3.set_title('Kustomisasi Horizontal Bar Chart - 2023')
    ax3.set_xlabel('Jumlah Penjualan')
    ax3.set_ylabel('Merk')
    ax3.barh(y, sales_2023, color='maroon', edgecolor = 'black')
    ax3.grid(axis='x', linestyle = '--', alpha=0.6)

    #label nilai
    for i, v in enumerate(sales_2023):
        ax3.text(v + 5, i, str(v), va = 'center')
    
    st.pyplot(fig3)


    #stacked
    st.subheader('Kustomisasi Horizontal Bar Chart')

    fig4, ax4 = plt.subplots()

    ax4.set_yticks(y)
    ax4.set_yticklabels(brands)
    ax4.set_title('Stacked Horizontal Bar Chart - 2023')
    ax4.set_xlabel('Jumlah Penjualan')
    ax4.set_ylabel('Merk')
    ax4.barh(y, sales_2023, label = '2023', color='maroon', edgecolor = 'black')
    ax4.barh(y, sales_2024, left=sales_2023, label = '2024', color='yellow', edgecolor = 'black')
    ax4.legend()
    ax4.grid(axis='x', linestyle='--', alpha=0.6)

    st.pyplot(fig4)


#multiple
else:
    st.subheader('Multiple Horizontal Bar Chart')

    fig5, ax5 = plt.subplots()

    ax5.set_yticks(y)
    ax5.set_yticklabels(brands)
    ax5.set_title('Multiple Horizontal Bar Chart - 2025')
    ax5.set_xlabel('Jumlah Penjualan')
    ax5.set_ylabel('Merk')
    ax5.barh(y - bar_width/2, sales_2023, height=bar_width, label = '2023')
    ax5.barh(y + bar_width/2, sales_2024, height=bar_width, label = '2024')
    ax5.grid(axis='x', linestyle = '--', alpha=0.6)
    ax5.legend()

    st.pyplot(fig5)


    #stacked
    st.subheader('Multiple Stacked Horizontal Bar Chart')

    fig6, ax6 = plt.subplots()

    ax6.set_yticks(y)
    ax6.set_yticklabels(brands)
    ax6.set_title('Multiple Stacked Horizontal Bar Chart - 2023')
    ax6.set_xlabel('Jumlah Penjualan')
    ax6.set_ylabel('Merk')
    ax6.barh(y, sales_2023, label = '2023')
    ax6.barh(y, sales_2024, label = '2024', left=sales_2023)
    ax6.grid(axis='x', linestyle='--', alpha=0.6)
    ax6.legend()

    st.pyplot(fig6)