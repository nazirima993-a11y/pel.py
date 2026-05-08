import streamlit as st
import datetime

# Setup Page
st.set_page_config(page_title="BERDESUP DELIVERY", layout="centered")

if 'page' not in st.session_state:
    st.session_state.page = 'page1'

def go_to(page_name):
    st.session_state.page = page_name

# --- PAGE 1: UTAMA ---
if st.session_state.page == 'page1':
    st.title("🚀 BERDESUP DELIVERY")
    st.write("Selamat Datang ke Sistem Penghantaran")
    
    if st.button("DAFTAR JOB BARU"):
        go_to('page2')

# --- PAGE 2: DAFTAR JOB ---
elif st.session_state.page == 'page2':
    st.title("📝 DAFTAR JOB")
    
    # Maklumat Asas
    nama = st.text_input("Nama Pelanggan")
    kategori = st.selectbox("Kategori", ["Motor", "Kereta", "4x4"])
    
    st.write("---")
    
    # Bahagian Alamat
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📍 Pick Up")
        alamat_p = st.text_input("Alamat (P)")
        tel_p = st.text_input("No. Tel (P)")
    
    with col2:
        st.subheader("🏁 Drop Off")
        alamat_d = st.text_input("Alamat (D)")
        tel_d = st.text_input("No. Tel (D)")

    st.write("---")

    # Kira Harga & Maps
    jarak = st.number_input("Masukkan Jarak (KM)", min_value=0.0, step=0.1)
    harga = jarak * 1.50 # Harga RM1.50 per KM
    st.subheader(f"💰 Harga Delivery: RM {harga:.2f}")

    if alamat_p and alamat_d:
        url = f"https://www.google.com/maps/dir/{alamat_p}/{alamat_d}"
        st.markdown(f"### [🌍 KLIK UNTUK GOOGLE MAPS]({url})", unsafe_allow_html=True)

    st.write("---")

    # Butang Navigasi
    c1, c2 = st.columns(2)
    with c1:
        if st.button("⬅️ KEMBALI"):
            go_to('page1')
    with c2:
        if st.button("✅ SIMPAN JOB"):
            if jarak > 0:
                st.success(f"Job {nama} berjaya didaftarkan!")
            else:
                st.warning("Sila masukkan jarak (KM) dulu.")
