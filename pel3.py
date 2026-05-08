import streamlit as st
import datetime

# 1. Setup Halaman
st.set_page_config(page_title="BERDESUP DELIVERY", layout="centered")

# 2. Sistem Navigasi
if 'page' not in st.session_state:
    st.session_state.page = 'page1'

def go_to(page_name):
    st.session_state.page = page_name

# --- PAGE 1: UTAMA ---
if st.session_state.page == 'page1':
    st.title("🚀 BERDESUP DELIVERY")
    st.write("Sistem Pendaftaran Job")
    
    if st.button("DAFTAR JOB BARU", use_container_width=True):
        go_to('page2')

# --- PAGE 2: BORANG DAFTAR ---
elif st.session_state.page == 'page2':
    st.title("📝 DAFTAR JOB")
    
    # Input Maklumat
    nama = st.text_input("Nama Pelanggan")
    kategori = st.selectbox("Kategori", ["Motor", "Kereta", "4x4"])
    tarikh = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    st.write(f"Tarikh/Masa: {tarikh}")

    st.write("---")
    
    # Bahagian Alamat
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📍 Pick Up")
        p = st.text_input("Alamat Pick-up")
    with col2:
        st.subheader("🏁 Drop Off")
        d = st.text_input("Alamat Drop-off")

    st.write("---")

    # Kira Harga & Google Maps
    jarak = st.number_input("Masukkan Jarak (KM)", min_value=0.0, step=0.1)
    harga = jarak * 1.50
    st.subheader(f"💰 Harga Delivery: RM {harga:.2f}")

    if p and d:
        url = f"https://www.google.com/maps/dir/{p}/{d}"
        st.markdown(f"### [🌍 KLIK UNTUK GOOGLE MAPS]({url})")

    st.write("---")

    # Butang Simpan
    if st.button("✅ SIMPAN & HANTAR", use_container_width=True):
        if jarak > 0 and nama:
            st.success(f"Job {nama} Berjaya Disimpan!")
        else:
            st.error("Sila masukkan Nama dan Jarak!")
    
    if st.button("⬅️ KEMBALI KE MENU"):
        go_to('page1')