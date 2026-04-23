import streamlit as st
from utils.ui import apply_modern_sidebar

st.set_page_config(page_title="Tentang Model AI", page_icon="🤖", layout="wide")
apply_modern_sidebar()
st.title("Tentang Model Kecerdasan Buatan")
st.markdown("Dokumentasi teknis mengenai arsitektur Machine Learning yang digunakan dalam sistem ini.")
st.divider()

col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("Arsitektur Inti: EfficientNet-B3")
    st.write("""
    Sistem ini ditenagai oleh **EfficientNet-B3**, sebuah arsitektur Convolutional Neural Network (CNN) mutakhir. 
    Kami memilih EfficientNet karena kemampuannya menyeimbangkan antara akurasi yang tinggi dan efisiensi komputasi, 
    menjadikannya sangat ideal untuk mengekstraksi fitur halus pada citra medis tanpa membebani server.
    """)
    
    st.subheader("Pipeline Preprocessing")
    st.write("Sebelum dianalisis, setiap citra melewati serangkaian tahap standar medis:")
    st.markdown("""
    1. **Auto-Crop:** Membuang area batas hitam berlebih.
    2. **Resize:** Normalisasi ukuran menjadi 224x224 piksel.
    3. **CLAHE (Contrast Limited Adaptive Histogram Equalization):** Memperjelas kontras pembuluh darah dan kekeruhan lensa.
    4. **Gaussian Blur:** Mengurangi noise (bintik) pada gambar.
    5. **Z-Score Normalization:** Penyesuaian distribusi nilai piksel.
    """)

with col2:
    st.subheader("Kemampuan Deteksi (4 Kelas)")
    st.info("""
    Model telah dilatih menggunakan metode **Stratified Split** untuk mengenali dan mengklasifikasikan 4 kondisi utama:
    - **Katarak**
    - **Diabetic Retinopathy**
    - **Glaukoma**
    - **Normal**
    """)
    
    st.subheader("Transparansi Model (Grad-CAM)")
    st.write("""
    Untuk menghindari sifat *"Black Box"* (di mana AI hanya memberikan hasil tanpa penjelasan), 
    sistem ini dilengkapi dengan teknologi **Grad-CAM (Gradient-weighted Class Activation Mapping)**. 
    
    Grad-CAM memproyeksikan peta panas (heatmap) visual yang menyoroti area spesifik pada mata yang paling mempengaruhi model dalam membuat keputusannya.
    """)