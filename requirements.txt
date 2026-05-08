import streamlit as st
import urllib.parse
import datetime

# Setup Navigasi
if 'page' not in st.session_state:
    st.session_state.page = 'page1'

def go_to(p):
    st.session_state.page = p
    st.rerun()

# --- PAGE 1 ---
if st.session_state.page == 'page1':
    st.title("BERDESUP DELIVERY")
    if st.button("DAFTAR JOB", use_container_width=True):
        go_to('page2')
    if st.button("MONITORING JOB", use_container_width=True):
        st.write("Page 7")

# --- PAGE 2 ---
elif st.session_state.page == 'page2':
    st.title("DAFTAR JOB")
    
    # Ikut Lakaran: Nama, Kategori, Tarikh, Masa
    nama = st.text_input("Nama")
    kategori = st.selectbox("Kategori", ["Motor", "Kereta", "4x4"])
    tarikh_masa = st.text_input("Tarikh / Masa", value=datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))

    st.write("---")
    
    # Bahagian Pick Up & Drop
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Pick Up")
        alamat_p = st.text_input("Alamat (P)")
        tel_p = st.text_input("No. Tel (P)")
        kawasan_p = st.text_input("Kawasan (P)")
    with col2:
        st.subheader("Drop")
        alamat_d = st.text_input("Alamat (D)")
        tel_d = st.text_input("No. Tel (D)")
        kawasan_d = st.text_input("Kawasan (D)")

    st.write("---")

    # --- TAMBAHAN BUTANG GOOGLE MAPS (IKUT ARAHAN) ---
    if alamat_p and alamat_d:
        maps_link = f"https://www.google.com/maps/dir/?api=1&origin={urllib.parse.quote(alamat_p)}&destination={urllib.parse.quote(alamat_d)}&travelmode=driving"
        st.link_button("🚀 BUKA GOOGLE MAPS UNTUK KIRA JARAK", maps_link, use_container_width=True)
    
    # Input Jarak & Pengiraan Harga (Ikut Lakaran)
    jarak = st.number_input("Jarak (Google Maps)", min_value=0.0, step=0.1)
    
    # Logik Harga Ikut Lakaran
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

    st.subheader(f"Harga: RM {harga:.2f}")
    
    st.write("Nota: Pembayaran ketika sampai item")
    setuju = st.checkbox("Saya bersetuju dengan harga di atas")
    
    # ID JOB (Auto)
    st.text_input("ID JOB", value=f"{kategori[:3].upper()}-AUTO", disabled=True)

    # Butang Navigasi Bawah
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Back"):
            go_to('page1')
    with c2:
        if st.button("Submit"):
            if setuju:
                st.success("Data disimpan ke Page 3")
            else:
                st.error("Sila tanda setuju harga")