import streamlit as st
from pathlib import Path
from PIL import Image
import time

from utils.helper import plot_probability_chart
from utils.preprocess import process_eye_image 
from utils.model import load_model, predict, generate_gradcam 
from utils.database import init_db, save_prediction, get_history

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
MODELS_DIR = BASE_DIR / "models"
MODEL_PATH = MODELS_DIR / "model_katarak.pt" 

st.set_page_config(page_title="Deteksi Dini Katarak", page_icon="🎗️", layout="wide")

st.title("Pengembangan Model Deep Learning untuk Deteksi Dini Katarak pada Citra Digital Mata: Studi Kasus Penanganan Ketidakseimbangan Data dan Generalisasi Real-World")
st.markdown("Silakan unggah foto fundus atau slit-lamp untuk menganalisis indikasi katarak.")
st.divider()

@st.cache_resource
def get_pytorch_model():
    return load_model(str(MODEL_PATH))

model_ai, device = get_pytorch_model()
col1, col2 = st.columns(2, gap="large")
with col1:
    st.subheader("1. Unggah & Preprocessing")
    uploaded_file = st.file_uploader("Pilih foto fundus/slit-lamp", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        with st.expander("Detail Proses Citra", expanded=True):
            img_visual, img_tensor = process_eye_image(image)
            st.image(img_visual, caption="Hasil Preprocessing", use_container_width=True)
        st.session_state['tensor_model'] = img_tensor
        st.session_state['image_for_ui'] = img_visual

with col2:
    st.subheader("2. Hasil Analisis")
    if uploaded_file is not None:
        if st.button("Analisis Gambar Sekarang", type="primary"):
            if model_ai is not None:
                hasil_prediksi = predict(model_ai, st.session_state['tensor_model'], device)
                
                prediksi_utama = list(hasil_prediksi.keys())[0]
                nilai_utama = list(hasil_prediksi.values())[0]

                save_prediction(prediksi_utama, nilai_utama, uploaded_file.name)
                
                st.success(f"Analisis Selesai: {prediksi_utama} ({nilai_utama:.1f}%)")
                plot_probability_chart(hasil_prediksi)
                
                with st.expander("🔍 Lihat Interpretasi Model (Grad-CAM)"):
                    heatmap_img = generate_gradcam(model_ai, st.session_state['tensor_model'], st.session_state['image_for_ui'], device)
                    st.image(heatmap_img, use_container_width=True)
            else:
                st.error("Model tidak ditemukan.")
    else:
        st.info("Unggah gambar untuk memulai.")

st.divider()
st.subheader("Riwayat Prediksi Terakhir")
df_history = get_history()
if not df_history.empty:
    st.dataframe(
        df_history, 
        use_container_width=True,
        column_config={
            "tanggal": "Waktu Analisis",
            "hasil_prediksi": "Hasil Diagnosis",
            "confidence": st.column_config.NumberColumn("Keyakinan (%)", format="%.2f%%")
        }
    )
else:
    st.write("Belum ada riwayat analisis.")