#import library
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#Judul
st.title("Praktikum 8 Visualisasi Data")
st.subheader("Pie Chart & Area Chart")
st.write("**Kelompok 23**")
st.markdown("""
    - Amru Abdurrahman Azzam - 0110122322
    - Hayatunnisa - 0110222118
    - Nurul Maedatul Awaliah - 0110122222
 """)


#dataset pie chart
kegiatan = ['Olahraga', 'Seni', 'Musik', 'Debat']
persentase = [30, 20, 25, 25]

#dataset area chart
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
shoes = [500, 600, 700, 800, 650, 700, 750, 800, 850]
sandals = [300, 350, 400, 450, 500, 480, 520, 550, 600]
socks = [200, 250, 300, 350, 400, 380, 420, 450, 500]


#filter kategori
kategori = st.selectbox(
    "Pilih Kategori Visualisasi",
    ["Basic Chart", "Kustomisasi Grafik", "Multiple Chart"]
)


#grafik basic
if kategori == "Basic Chart":
    #pie chart
    st.subheader("Basic Pie Chart")

    fig1, ax1 = plt.subplots()
    ax1.pie(
        persentase,
        labels=kegiatan,
        autopct='%1.1f%%',
        startangle=140
    )
    ax1.set_title("Persentase Partisipasi Siswa")
    st.pyplot(fig1)

    #area chart
    st.subheader("Basic Area Chart")

    fig2, ax2 = plt.subplots()
    ax2.fill_between(months, shoes, alpha=0.4)
    ax2.set_title("Basic Area Chart: Monthly Sales")
    ax2.set_xlabel("Months")
    ax2.set_ylabel("Units Sold")
    st.pyplot(fig2)


#grafik kustomisasi
elif kategori == "Kustomisasi Grafik":
    #pie chart
    st.subheader("Customized Pie Chart")

    colors = ['#FFF44F', 'lightskyblue', '#5e7561', 'pink']
    explode = (0.1, 0, 0, 0)

    fig3, ax3 = plt.subplots()
    ax3.pie(
        persentase,
        labels=kegiatan,
        colors=colors,
        autopct='%1.1f%%',
        startangle=140,
        explode=explode,
        shadow=True
    )
    ax3.set_title("Persentase Partisipasi Siswa (Customized)")
    ax3.legend(title="Kegiatan")
    st.pyplot(fig3)

    #area chart
    st.subheader("Customized Area Chart")

    fig4, ax4 = plt.subplots()
    ax4.fill_between(months, shoes, alpha=0.5, label='Shoes')
    ax4.fill_between(months, sandals, alpha=0.5, label='Sandals')
    ax4.set_title("Customized Area Chart: Monthly Sales")
    ax4.set_xlabel("Months")
    ax4.set_ylabel("Units Sold")
    ax4.legend()
    ax4.grid(axis='y', linestyle='--', alpha=0.6)
    st.pyplot(fig4)


#grafik multiple
else:
    #pie chart
    st.subheader("Multiple Pie Chart")

    fig5, axs = plt.subplots(1, 2, figsize=(12, 5))

    kegiatan_1 = ['Olahraga', 'Seni']
    persentase_1 = [40, 60]

    kegiatan_2 = ['Musik', 'Debat']
    persentase_2 = [50, 50]

    axs[0].pie(
        persentase_1,
        labels=kegiatan_1,
        autopct='%1.1f%%',
        startangle=140
    )
    axs[0].set_title("Partisipasi Kelompok 1")

    axs[1].pie(
        persentase_2,
        labels=kegiatan_2,
        autopct='%1.1f%%',
        startangle=140
    )
    axs[1].set_title("Partisipasi Kelompok 2")

    plt.suptitle("Perbandingan Partisipasi Siswa")
    st.pyplot(fig5)

    #area chart
    st.subheader("Multiple Area Chart")

    fig6, ax6 = plt.subplots()
    ax6.fill_between(months, shoes, alpha=0.4, label='Shoes')
    ax6.fill_between(months, sandals, alpha=0.4, label='Sandals')
    ax6.fill_between(months, socks, alpha=0.4, label='Socks')
    ax6.set_title("Multiple Area Chart: Monthly Sales")
    ax6.set_xlabel("Months")
    ax6.set_ylabel("Units Sold")
    ax6.legend()
    ax6.grid(axis='y', linestyle='--', alpha=0.6)
    st.pyplot(fig6)