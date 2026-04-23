import streamlit as st
from utils.ui import apply_modern_sidebar

st.set_page_config(page_title="Edukasi Penyakit Mata", page_icon="📚", layout="wide")
apply_modern_sidebar()
st.title("Informasi & Edukasi Penyakit Mata")
st.markdown("Kenali berbagai kondisi kesehatan mata, gejala, dan cara pencegahannya.")
st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["Katarak", "Diabetic Retinopathy", "Glaukoma", "Mata Normal"])

with tab1:
    st.header("Katarak")
    st.write("**Deskripsi:** Kekeruhan pada lensa mata yang biasanya jernih. Seperti melihat melalui jendela yang berkabut.")
    st.write("**Gejala Umum:**")
    st.markdown("- Pandangan kabur atau redup\n- Sulit melihat di malam hari\n- Sensitif terhadap cahaya dan silau\n- Warna terlihat memudar")
    st.info("💡 **Pencegahan & Penanganan:** Pemeriksaan mata rutin, melindungi mata dari sinar UV, dan operasi pengangkatan lensa yang keruh jika sudah mengganggu aktivitas.")

with tab2:
    st.header("Diabetic Retinopathy")
    st.write("**Deskripsi:** Komplikasi diabetes yang memengaruhi mata. Disebabkan oleh kerusakan pembuluh darah pada jaringan peka cahaya di bagian belakang mata (retina).")
    st.write("**Gejala Umum:**")
    st.markdown("- Bintik-bintik atau benang gelap yang melayang di penglihatan (floaters)\n- Penglihatan berfluktuasi\n- Area penglihatan yang gelap atau kosong")
    st.info("💡 **Pencegahan & Penanganan:** Mengontrol kadar gula darah, tekanan darah, dan kolesterol dengan ketat adalah cara terbaik untuk mencegah kondisi ini.")

with tab3:
    st.header("Glaukoma")
    st.write("**Deskripsi:** Kelompok kondisi mata yang merusak saraf optik, yang kerusakannya sering disebabkan oleh tekanan tinggi yang tidak normal pada mata.")
    st.write("**Gejala Umum:**")
    st.markdown("- Sering kali tidak ada gejala pada tahap awal (Pencuri penglihatan diam-diam)\n- Pada tahap lanjut: kehilangan penglihatan tepi (tunnel vision)\n- Sakit mata parah dan mual (pada jenis glaukoma akut)")
    st.info("💡 **Pencegahan & Penanganan:** Deteksi dini melalui pemeriksaan tekanan bola mata rutin sangat krusial karena kerusakan saraf optik tidak dapat diperbaiki.")

with tab4:
    st.header("Mata Normal")
    st.write("**Deskripsi:** Kondisi mata yang sehat, di mana lensa jernih, tekanan bola mata stabil, dan pembuluh darah pada retina berfungsi dengan baik tanpa adanya penyumbatan atau kebocoran.")
    st.success("✅ **Tips Menjaga Kesehatan Mata:**\n- Konsumsi makanan bergizi (kaya vitamin A, C, E, dan Omega-3)\n- Istirahatkan mata dari layar gadget (Aturan 20-20-20)\n- Gunakan kacamata hitam pelindung UV saat berada di luar ruangan.")