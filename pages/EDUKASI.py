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
    st.write("**Deskripsi:** Katarak adalah kondisi medis yang ditandai penglihatan kabur akibat lensa mata yang semula jernih menjadi keruh. Lensa mata, yang terletak di belakang iris dan pupil, berfungsi memfokuskan cahaya ke retina agar kamu dapat melihat dengan jelas. Ketika katarak berkembang, lensa mata menjadi semakin keruh, menghalangi cahaya untuk mencapai retina dan menyebabkan gangguan penglihatan.")
    
    st.header("Penyebab Katarak")
    st.write("**Penuaan alami:** Ini adalah penyebab paling umum. Seiring bertambahnya usia, lensa mata secara bertahap menebal dan kehilangan fleksibilitasnya. Akibatnya, protein dalam lensa mulai menggumpal dan menghalangi cahaya yang seharusnya masuk ke retina.")
    st.write("**Perubahan struktur lensa mata:** Lensa yang sebagian besar terdiri dari air dan protein akan mengalami perubahan seiring waktu. Gumpalan protein ini menghambat cahaya yang masuk ke retina, menyebabkan pandangan menjadi buram dan tidak setajam biasanya.")
    st.write("**Perubahan warna lensa:** Pada tahap awal, lensa mungkin berubah menjadi kuning atau kecokelatan secara ringan. Namun, perubahan ini akan bertambah parah seiring waktu, sehingga penglihatan makin terganggu.")
    
    st.header("Faktor Risiko Katarak")
    st.write("Terdapat beberapa faktor yang bisa meningkatkan risiko katarak, antara lain:")
    st.markdown("- Penuaan. Penuaan adalah penyebab tersering dari kekeruhan lensa atau katarak.\n- Riwayat trauma. Lensa mata yang pernah mengalami trauma, seperti masuknya serpihan material tajam ke mata, terbentur bola, kembang api, dapat membuat katarak timbul lebih cepat.\n- Infeksi saat kehamilan. Jika ibu saat hamil mengidap infeksi, khususnya rubella, dapat menjadi penyebab utama terjadinya katarak kongenital pada anak yang dilahirkan. Katarak kongenital dapat terjadi pada salah satu atau kedua mata anak.\n- Mengonsumsi obat-obatan tertentu dalam jangka waktu lama, seperti obat kortikosteroid dan amiodaron, dapat memicu katarak.")

    st.header("Gejala Katarak")
    st.write("Gejala katarak berkembang secara bertahap dan mungkin tidak terasa pada awalnya. Beberapa gejala umum katarak meliputi:")
    st.markdown("- Penglihatan kabur atau buram\n- Sensitif terhadap cahaya (silau)\n- Penglihatan ganda\n- Kesulitan melihat di malam hari")

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