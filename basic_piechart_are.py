import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Konfigurasi halaman
st.set_page_config(page_title="Basic Charts", layout="centered")
st.title("📈 Praktikum 8: Pie Chart & Area Chart")
st.markdown("""
**Kelompok 31**
- Ahmad Yasin (0110222094)
- Muhammad Lutfi Alfian (0110222078)
- Farhan Ijayansyah (0110222098)
""")

# ==================== BAGIAN 1: PIE CHART ====================
st.header("1. Pie Chart dengan Matplotlib")

# Data untuk pie chart
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
sizes = [15, 30, 45, 10]
# 'explode' memisahkan irisan ke-2 ('Hogs')[citation:7][citation:9]
explode = (0, 0.1, 0, 0)

# Membuat figure dan axes
fig1, ax1 = plt.subplots()
# Membuat pie chart[citation:3]
ax1.pie(sizes,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',  # Format string untuk menampilkan persentase[citation:3][citation:7]
        shadow=True,       # Menambahkan bayangan[citation:9]
        startangle=90)     # Memulai irisan pertama dari sudut 90 derajat[citation:9]
ax1.axis('equal')  # Membuat aspek rasio sama sehingga pie berbentuk lingkaran sempurna[citation:7]

st.pyplot(fig1)

# ==================== BAGIAN 2: AREA CHART (2 Metode) ====================
st.header("2. Area Chart")

# --- Metode 1: Area Chart Bawaan Streamlit (Mudah) ---
st.subheader("Metode 1: Menggunakan `st.area_chart`")
st.caption("Cara sederhana dengan data dataframe[citation:1][citation:2].")

# Membuat data contoh
chart_data = pd.DataFrame({
    'Bulan': np.arange(1, 13),
    'Pendapatan': [5, 9, 6, 6, 10, 7, 6, 4, 4, 5, 6, 4],
    'Pengeluaran': [6, 6, 8, 3, 6, 9, 7, 8, 6, 6, 4, 8]
}).set_index('Bulan')  # Set indeks untuk dijadikan sumbu-x[citation:2]

# Menampilkan area chart
st.area_chart(chart_data)

# --- Metode 2: Area Chart dengan Matplotlib (Lebih Kustom) ---
st.subheader("Metode 2: Menggunakan Matplotlib `fill_between`")
st.caption("Memberikan kontrol lebih detail untuk mengisi area[citation:4][citation:6][citation:10].")

fig2, ax2 = plt.subplots(figsize=(8, 4))
x = chart_data.index
y_income = chart_data['Pendapatan']
y_expenses = chart_data['Pengeluaran']

# Plot garis
ax2.plot(x, y_income, color='green', label='Pendapatan')
ax2.plot(x, y_expenses, color='red', label='Pengeluaran')

# Parameter penting: Mengisi area antara dua garis[citation:6]
# where & interpolate: Mengisi area dengan rapi bahkan saat garis bersilangan[citation:4][citation:10]
ax2.fill_between(x, y_income, y_expenses,
                 where=(y_income > y_expenses), # type: ignore
                 interpolate=True,
                 color='green', alpha=0.3,
                 label='Surplus (Pendapatan > Pengeluaran)')

ax2.fill_between(x, y_income, y_expenses,
                 where=(y_income <= y_expenses), # type: ignore
                 interpolate=True,
                 color='red', alpha=0.3,
                 label='Defisit (Pendapatan ≤ Pengeluaran)')

ax2.set_xlabel('Bulan')
ax2.set_ylabel('Jumlah (dalam unit)')
ax2.set_title('Perbandingan Pendapatan dan Pengeluaran')
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.7)

st.pyplot(fig2)

# ==================== BAGIAN 3: TABEL PENJELASAN PARAMETER ====================
st.header("3. Tabel Penjelasan Parameter Kunci")

st.markdown("""
Berikut adalah penjelasan untuk beberapa parameter penting yang digunakan dalam kode di atas.
""")

# Data untuk tabel
parameter_data = {
    "Fungsi & Parameter": [
        "**`plt.pie()` / `ax.pie()`**",
        "&nbsp;&nbsp;`x` (atau `sizes`)",
        "&nbsp;&nbsp;`labels`",
        "&nbsp;&nbsp;`autopct`",
        "&nbsp;&nbsp;`explode`",
        "&nbsp;&nbsp;`startangle`",
        "",
        "**`plt.fill_between()` / `ax.fill_between()`**",
        "&nbsp;&nbsp;`x`",
        "&nbsp;&nbsp;`y1`",
        "&nbsp;&nbsp;`y2`",
        "&nbsp;&nbsp;`where`",
        "&nbsp;&nbsp;`interpolate`",
        "&nbsp;&nbsp;`alpha`",
        "",
        "**`st.area_chart()`**",
        "&nbsp;&nbsp;`data`",
        "&nbsp;&nbsp;`x`",
        "&nbsp;&nbsp;`y`",
    ],
    "Fungsi / Penjelasan": [
        "**Fungsi utama untuk membuat Pie Chart**[citation:3].",
        "Array data numerik yang menentukan ukuran setiap irisan pie[citation:3].",
        "List string untuk memberi label pada setiap irisan[citation:3][citation:9].",
        "**Menambahkan teks persentase di dalam irisan.** Format `'%1.1f%%'` artinya angka float dengan 1 digit desimal diikuti tanda persen[citation:3][citation:7][citation:9].",
        "Array untuk 'meledakkan' (memisahkan) irisan dari pusat. Nilai `0.1` artinya dipisahkan sejauh 10% radius[citation:7][citation:9].",
        "Sudut (dalam derajat) di mana irisan pertama akan dimulai. `90` memulai dari arah atas[citation:9].",
        "",
        "**Fungsi utama untuk mengisi area antara dua kurva horizontal**[citation:6].",
        "Koordinat titik-titik pada sumbu-X[citation:6].",
        "Koordinat Y dari kurva pertama (atau kurva atas)[citation:6].",
        "Koordinat Y dari kurva kedua. Default-nya adalah `0` (sumbu-X), sehingga mengisi area di bawah kurva `y1`[citation:4][citation:6].",
        "**Array boolean** untuk memilih area mana yang akan diisi. Contoh: `where=(y1 > y2)` hanya mengisi area dimana `y1` lebih besar dari `y2`[citation:6][citation:10].",
        "Jika `True`, menghitung titik persilangan antara `y1` dan `y2` untuk mengisi area dengan lebih rapi, terutama jika `where` digunakan[citation:4][citation:6][citation:10].",
        "**Tingkat transparansi** warna isian (0=transparan sepenuhnya, 1=padat sepenuhnya)[citation:4].",
        "",
        "**Fungsi bawaan Streamlit** untuk membuat Area Chart dengan cepat dari DataFrame[citation:1][citation:2].",
        "Data yang akan diplot (biasanya DataFrame).",
        "Nama kolom untuk sumbu-X. Jika `None`, akan menggunakan indeks DataFrame[citation:2].",
        "Nama kolom untuk sumbu-Y. Jika `None`, akan menggunakan semua kolom numerik lainnya[citation:2].",
    ]
}

# Menampilkan tabel
df_params = pd.DataFrame(parameter_data)
st.table(df_params)

st.caption("Dibuat dengan Streamlit dan Matplotlib.")