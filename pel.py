import streamlit as st
import urllib.parse
import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="BERDESUP DELIVERY SYSTEM", layout="centered")

# Inisialisasi status halaman (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'page1'

# Fungsi Navigasi
def pindah_halaman(nama_halaman):
    st.session_state.page = nama_halaman
    st.rerun()

# ==========================================
# PAGE 1: MENU UTAMA
# ==========================================
if st.session_state.page == 'page1':
    st.markdown("<h1 style='text-align: center;'>🚀 BERDESUP DELIVERY</h1>", unsafe_allow_html=True)
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("① DAFTAR JOB", use_container_width=True, type="primary"):
            pindah_halaman('page2')
            
    with col2:
        if st.button("② MONITORING JOB", use_container_width=True):
            st.info("Halaman Monitoring (Page 7) dalam pembangunan.")

# ==========================================
# PAGE 2: BORANG DAFTAR JOB
# ==========================================
elif st.session_state.page == 'page2':
    st.markdown("## 📝 DAFTAR JOB")
    
    with st.form("job_form"):
        # Maklumat Pelanggan
        nama = st.text_input("Nama Pelanggan")
        kategori = st.selectbox("Kategori Kenderaan", ["Motor", "Kereta", "4x4"])
        tarikh_jam = st.text_input("Tarikh & Jam", value=datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
        
        st.write("---")
        
        # Lokasi Pick Up & Drop
        col_p, col_d = st.columns(2)
        with col_p:
            st.markdown("### 📍 Pick Up")
            alamat_p = st.text_input("Alamat (P)")
            tel_p = st.text_input("No Tel (P)")
            kawasan_p = st.text_input("Kawasan (P)")
            
        with col_d:
            st.markdown("### 🏁 Drop")
            alamat_d = st.text_input("Alamat (D)")
            tel_d = st.text_input("No Tel (D)")
            kawasan_d = st.text_input("Kawasan (D)")
            
        st.write("---")

        # Integrasi Google Maps
        st.write("🛰️ *Kiraan Jarak Melalui Google Maps:*")
        if alamat_p and alamat_d:
            url = 
       f"https://www.google.com/maps/dir/{alamat_p}
       /{alamat_d}".replace("","+")
            st.link_button("🚀 BUKA GOOGLE MAPS (KLIK SINI)", url, use_container_width=True)
        else:
            st.caption("Sila isi alamat P dan D untuk menjana pautan Google Maps.")

        # Input Jarak & Pengiraan Harga
        jarak = st.number_input("Masukkan Jarak (KM) dari Google Maps", min_value=0.0, step=0.1)
        
        # LOGIK HARGA (DARI LAKARAN)
        harga = 0.0
        if kategori == "Motor":
            base = 5.0 if jarak <= 5 else 2.5
            harga = base + (1.0 * jarak)
        elif kategori == "Kereta":
            base = 7.5 if jarak <= 10 else 5.0
            harga = base + (1.5 * jarak)
        elif kategori == "4x4":
            base = 15.0 if jarak <= 10 else 10.0
            harga = base + (2.3 * jarak)
            
        st.subheader(f"💵 ESTIMASI HARGA: RM {harga:.2f}")
        
        st.write("⚠️ Pembayaran ketika item sampai (COD)")
        setuju = st.checkbox("Saya bersetuju dengan harga di atas")
        
        # Butang Submit Form
        submit_btn = st.form_submit_button("SUBMIT ✅", use_container_width=True)
        
        if submit_btn:
            if setuju and nama and jarak > 0:
                st.success(f"Job Berjaya Didaftar! ID: {kategori[:3].upper()}-{datetime.datetime.now().strftime('%H%M%S')}")
                # Logik simpan ke Page 3 (Database) akan diletakkan di sini
            else:
                st.error("Sila lengkapkan maklumat, isi jarak, dan tanda persetujuan.")

    # Butang Kembali ke Page 1 (Diluar Form)
    if st.button("⬅️ KEMBALI KE MENU"):
        pindah_halaman('page1')