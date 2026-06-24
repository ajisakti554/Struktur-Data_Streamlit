import streamlit as st
# Mengatur konfigurasi dasar halaman web
st.set_page_config(page_title="Aplikasi Pertamaku", page_icon="n")
# nn Bagian Utama nnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
st.title("n Halo, Streamlit!")
st.write("Ini adalah aplikasi web sederhana menggunakan sintaks dasar Streamlit.")
# nn Bagian Sidebar nnnnnnnnnnnnnnnnnnnnnnnnnnnn
st.sidebar.header("Panel Pengaturan")
nama_pengguna = st.sidebar.text_input("Masukkan nama kamu:")
# nn Interaktivitas dengan Button nnnnnnnnnnnnnn
if st.button("Sapa Saya"):
    if nama_pengguna:
        st.success(f"Halo {nama_pengguna}, selamat datang di dunia Streamlit!")
    else:
        st.warning("Tolong isi nama kamu di sidebar terlebih dahulu.")