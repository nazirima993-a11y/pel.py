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
    col…
[16:04, 8/5/2026] Amir: import streamlit as st
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
    tarikh = date…
[17:26, 8/5/2026] Amir: maps_url = f"https://www.google.com/maps/dir/{alamat_p}/{alamat_d}".replace(" ", "+")
        st.link_button("🚀 BUKA GOOGLE MAPS (KLIK SINI)", maps_url, use_container_width=True)
[17:29, 8/5/2026] Amir: maps_url = f"https://www.google.com/maps/dir/{alamat_p}/{alamat_d}".replace(" ", "+")
        st.link_button("🚀 BUKA GOOGLE MAPS (KLIK SINI)", maps_url, use_container_width=True)
[17:31, 8/5/2026] Amir: # Integrasi Google Maps
    st.write("*🗺️ Kiraan Jarak Melalui Google Maps:*")
    if alamat_p and alamat_d:
        # Bina link Google Maps yang betul
        maps_url = f"https://www.google.com/maps/dir/{alamat_p}/{alamat_d}".replace(" ", "+")
        # Papar butang besar
        st.link_button("🚀 BUKA GOOGLE MAPS (KLIK SINI)", maps_url, use_container_width=True)
    else:
        st.info("Sila isi alamat P dan D untuk menjana pautan Google Maps.")
[17:32, 8/5/2026] Amir: # Integrasi Google Maps
st.write("*🗺️ Kiraan Jarak Melalui Google Maps:*")
if alamat_p and alamat_d:
    # Bina link Google Maps yang betul
    maps_url = f"https://www.google.com/maps/dir/{alamat_p}/{alamat_d}".replace(" ", "+")
    # Papar butang besar
    st.link_button("🚀 BUKA GOOGLE MAPS (KLIK SINI)", maps_url, use_container_width=True)
else:
    st.info("Sila isi alamat P dan D untuk menjana pautan Google Maps.")

st.divider()

# --- Bahagian ini mesti berada di LUAR blok if/else (sejajar ke kiri) ---
# Input Jarak & Pengiraan Harga
jarak = st.number_input("Masukkan Jarak (KM) dari Google Maps", min_value=0.0, step=0.1)

# LOGIK HARGA (DARI LAKARAN)
harga = 0.0
if kategori == "Motor":
    base = 5.0 if jarak <= 5 else 2.5
    harga = base + (1.0 * ja…
[17:40, 8/5/2026] Amir: # Ganti baris 66 dengan ini
if 'alamat_p' in locals() and 'alamat_d' in locals():
    if alamat_p and alamat_d:
        maps_url = f"https://www.google.com/maps/dir/{alamat_p}/{alamat_d}".replace(" ", "+")
        st.link_button("🚀 BUKA GOOGLE MAPS (KLIK SINI)", maps_url, use_container_width=True)
    else:
        st.info("Sila isi alamat P dan D untuk menjana pautan Google Maps.")
[17:42, 8/5/2026] Amir: # Tambah baris ini di atas 'if kategori == "Motor":'
if 'kategori' not in locals(): kategori = "Motor" 

if kategori == "Motor":
    # ... sambungan kod anda
[17:45, 8/5/2026] Amir: # --- Tambah pilihan kategori di sini ---
kategori = st.selectbox("Pilih Jenis Kenderaan:", ["Motor", "Kereta", "4x4"])

# LOGIK HARGA (DARI LAKARAN)
harga = 0.0
if kategori == "Motor":
[17:49, 8/5/2026] Amir: # --- LOGIK PENGIRAAN HARGA ---
kategori = st.selectbox("Pilih Jenis Kenderaan:", ["Motor", "Kereta", "4x4"])
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

# --- PAPARAN HARGA & PERSETUJUAN ---
st.subheader(f"💵 ESTIMASI HARGA: RM {harga:.2f}")
st.write("⚠️ Pembayaran ketika item sampai (COD)")
setuju = st.checkbox("Saya bersetuju dengan harga di atas")

# --- BUTANG SUBMIT ---
if st.button("🚀 SUBMIT TEMPAHAN"):
    if setuju and jarak > 0:
        st.success("Tempahan Berjaya Didaftar!")
    else:
        st.error("Sila tanda persetujuan dan pastikan jarak (KM) telah diisi.")
[17:57, 8/5/2026] Amir: import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Berdesup Delivery", layout="centered")

# --- SIDEBAR NAVIGASI ---
st.sidebar.title("🚚 Berdesup Delivery")
halaman = st.sidebar.radio("Navigasi", ["Utama", "Daftar Job", "Semak Status"])

# --- HALAMAN UTAMA ---
if halaman == "Utama":
    st.title("Selamat Datang ke Berdesup Delivery")
    st.write("Penghantaran pantas, harga berpatutan!")
    st.image("https://via.placeholder.com/800x400.png?text=Berdesup+Delivery+Banner") # Anda boleh ganti link gambar anda

# --- HALAMAN DAFTAR JOB ---
elif halaman == "Daftar Job":
    st.title("📋 Daftar Job Baharu")
    
    # Bahagian Input Maklumat Pelanggan
    st.subheader("Maklumat Pengirim & Penerima")
    nama_p = st.text_input("Nama Pengirim")
    tel_p = st.text_input("No. Telefon Pengirim")
    
    st.divider()
    
    # Bahagian Alamat
    alamat_p = st.text_input("📍 Alamat Pengambilan (P)")
    alamat_d = st.text_input("🏁 Alamat Penghantaran (D)")

    # --- INTEGRASI GOOGLE MAPS ---
    st.write("---")
    st.write("*🗺️ Kiraan Jarak Melalui Google Maps:*")
    if alamat_p and alamat_d:
        # Menjana link Google Maps secara automatik
        maps_url = f"https://www.google.com/maps/dir/{alamat_p}/{alamat_d}".replace(" ", "+")
        st.link_button("🚀 BUKA GOOGLE MAPS (KLIK SINI)", maps_url, use_container_width=True)
    else:
        st.info("Sila isi alamat (P) dan (D) untuk menjana pautan Google Maps.")

    st.divider()

    # Bahagian Input Jarak & Kenderaan
    jarak = st.number_input("Masukkan Jarak (KM) dari Google Maps", min_value=0.0, step=0.1)
    kategori = st.selectbox("Pilih Jenis Kenderaan:", ["Motor", "Kereta", "4x4"])

    # LOGIK PENGIRAAN HARGA
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

    # Paparan Harga & Persetujuan
    st.subheader(f"💵 ESTIMASI HARGA: RM {harga:.2f}")
    st.write("⚠️ Pembayaran ketika item sampai (COD)")
    setuju = st.checkbox("Saya bersetuju dengan harga dan maklumat di atas")

    # BUTANG SUBMIT
    if st.button("🚀 SUBMIT TEMPAHAN"):
        if setuju and jarak > 0:
            st.success(f"Tempahan untuk {nama_p} Berjaya Didaftar!")
            st.balloons()
        else:
            st.error("Sila pastikan jarak diisi dan kotak persetujuan ditanda.")

# --- HALAMAN SEMAK STATUS ---
elif halaman == "Semak Status":
    st.title("🔍 Semak Status Penghantaran")
    no_order = st.text_input("Masukkan ID Tempahan")
    if st.button("Semak"):
        st.info("Fungsi semakan akan dikemaskini sebaik sahaja pangkalan data disambungkan.")

# --- FOOTER ---
st.sidebar.write("---")
st.sidebar.write("© 2024 Berdesup Delivery Service")
