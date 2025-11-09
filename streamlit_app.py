import streamlit as st

# Judul aplikasi
st.title("Kalkulator Luas Segitiga")
st.text("Tugas oleh : Nugroho - 10 TJKT 1")

# Input dari pengguna
st.header("Masukkan nilai:")
alas = st.number_input("Masukkan panjang alas (cm):", min_value=0.0, step=0.1)
tinggi = st.number_input("Masukkan tinggi (cm):", min_value=0.0, step=0.1)

# Tombol untuk menghitung
if st.button("Hitung Luas"):
    luas = 0.5 * alas * tinggi
    st.success(f"Luas segitiga adalah: {luas:.2f} cm²")

# Informasi tambahan
st.info("Rumus luas segitiga = ½ × alas × tinggi")
