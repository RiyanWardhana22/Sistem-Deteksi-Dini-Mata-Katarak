import streamlit as st
from utils.ui import apply_modern_sidebar

st.set_page_config(page_title="Edukasi Penyakit Mata", page_icon="📚", layout="wide")
apply_modern_sidebar()

st.title("Informasi & Edukasi Penyakit Mata")
st.markdown("Kenali berbagai kondisi kesehatan mata, gejala, faktor risiko, dan cara penanganannya secara medis.")
st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["Katarak", "Diabetic Retinopathy", "Glaukoma", "Mata Normal"])
with tab1:
    st.header("Katarak")
    st.write("**Deskripsi:** Katarak adalah kondisi medis yang ditandai penglihatan kabur akibat lensa mata yang semula jernih menjadi keruh. Lensa mata, yang terletak di belakang iris dan pupil, berfungsi memfokuskan cahaya ke retina agar kamu dapat melihat dengan jelas. Ketika katarak berkembang, lensa mata menjadi semakin keruh, menghalangi cahaya untuk mencapai retina dan menyebabkan gangguan penglihatan.")
    
    st.subheader("Penyebab Katarak")
    st.write("**Penuaan alami:** Ini adalah penyebab paling umum. Seiring bertambahnya usia, lensa mata secara bertahap menebal dan kehilangan fleksibilitasnya. Akibatnya, protein dalam lensa mulai menggumpal dan menghalangi cahaya yang seharusnya masuk ke retina.")
    st.write("**Perubahan struktur lensa mata:** Lensa yang sebagian besar terdiri dari air dan protein akan mengalami perubahan seiring waktu. Gumpalan protein ini menghambat cahaya yang masuk ke retina, menyebabkan pandangan menjadi buram dan tidak setajam biasanya.")
    st.write("**Perubahan warna lensa:** Pada tahap awal, lensa mungkin berubah menjadi kuning atau kecokelatan secara ringan. Namun, perubahan ini akan bertambah parah seiring waktu, sehingga penglihatan makin terganggu.")
    
    st.subheader("Faktor Risiko Katarak")
    st.write("Terdapat beberapa faktor yang bisa meningkatkan risiko katarak, antara lain:")
    st.markdown("- **Penuaan.** Penuaan adalah penyebab tersering dari kekeruhan lensa atau katarak.\n- **Riwayat trauma.** Lensa mata yang pernah mengalami trauma, seperti masuknya serpihan material tajam ke mata, terbentur bola, kembang api, dapat membuat katarak timbul lebih cepat.\n- **Infeksi saat kehamilan.** Jika ibu saat hamil mengidap infeksi, khususnya rubella, dapat menjadi penyebab utama terjadinya katarak kongenital pada anak yang dilahirkan.\n- **Penggunaan obat tertentu.** Mengonsumsi obat-obatan dalam jangka waktu lama, seperti kortikosteroid, dapat memicu katarak.")

    st.subheader("Gejala Katarak")
    st.write("Gejala katarak berkembang secara bertahap dan mungkin tidak terasa pada awalnya. Beberapa gejala umum meliputi:")
    st.markdown("- Penglihatan kabur, redup, atau seperti tertutup kabut\n- Sensitif terhadap cahaya dan silau (halo di sekitar lampu)\n- Penglihatan ganda pada satu mata\n- Penurunan ketajaman warna (warna memudar/menguning)\n- Kesulitan melihat di malam hari")
    
    st.info("💡 **Penanganan medis:** Satu-satunya penanganan yang efektif untuk katarak yang sudah mengganggu aktivitas adalah prosedur operasi (Fakoemulsifikasi) untuk mengganti lensa keruh dengan lensa buatan (IOL).")

with tab2:
    st.header("Diabetic Retinopathy (Retinopati Diabetik)")
    st.write("**Deskripsi:** Retinopati Diabetik adalah komplikasi mikrovaskuler dari penyakit diabetes yang memengaruhi mata. Kondisi ini disebabkan oleh kerusakan pada pembuluh darah di jaringan peka cahaya di bagian belakang mata (retina). Jika tidak ditangani, kondisi ini dapat menyebabkan penumpukan cairan (edema makula), perdarahan di dalam mata, hingga kebutaan permanen.")
    
    st.subheader("Penyebab Retinopati Diabetik")
    st.write("**Gula Darah Tinggi Berkepanjangan:** Terlalu banyak glukosa dalam darah dari waktu ke waktu dapat menyumbat pembuluh darah kecil yang menutrisi retina, memutus suplai darahnya. Sebagai respons, mata mencoba menumbuhkan pembuluh darah baru. Namun, pembuluh darah baru ini rapuh dan mudah bocor atau pecah.")
    
    st.subheader("Faktor Risiko")
    st.write("Risiko mengalami komplikasi ini akan meningkat pada pasien yang memiliki kondisi berikut:")
    st.markdown("- **Durasi diabetes:** Semakin lama seseorang mengidap diabetes (tipe 1 atau tipe 2), semakin besar risiko terkena retinopati diabetik.\n- **Kontrol gula darah yang buruk:** Kadar HbA1c yang selalu tinggi mempercepat kerusakan pembuluh darah.\n- **Hipertensi dan Kolesterol Tinggi:** Menambah beban pada pembuluh darah retina yang sudah rapuh.\n- **Kehamilan:** Dapat memperburuk kondisi retinopati diabetik yang sudah ada sebelumnya.\n- **Merokok:** Merusak sirkulasi darah secara sistemik.")

    st.subheader("Gejala Retinopati Diabetik")
    st.write("Pada tahap awal, penderita sering kali tidak merasakan gejala apapun. Gejala biasanya baru muncul saat kondisi sudah parah, meliputi:")
    st.markdown("- Munculnya bintik-bintik atau garis gelap yang melayang pada penglihatan (*floaters*)\n- Penglihatan yang berfluktuasi (terkadang jelas, terkadang kabur)\n- Munculnya area gelap atau kosong di tengah penglihatan\n- Kesulitan membedakan warna\n- Kehilangan penglihatan mendadak")

    st.info("💡 **Penanganan medis:** Pengobatan meliputi kontrol ketat terhadap gula darah, suntikan obat ke dalam mata (Anti-VEGF) untuk menghentikan pertumbuhan pembuluh darah baru, terapi laser (Fotokoagulasi), atau operasi vitrektomi untuk mengangkat darah dari tengah mata.")

with tab3:
    st.header("Glaukoma")
    st.write("**Deskripsi:** Glaukoma adalah sekelompok penyakit mata yang ditandai dengan kerusakan pada saraf optik, yang menghubungkan mata ke otak. Kerusakan ini sering kali (meski tidak selalu) berkaitan dengan tekanan tinggi di dalam bola mata (Tekanan Intraokular/TIO). Glaukoma merupakan salah satu penyebab utama kebutaan ireversibel (tidak dapat disembuhkan) di seluruh dunia.")
    
    st.subheader("Penyebab Glaukoma")
    st.write("**Penumpukan Cairan Mata:** Bola mata secara konstan memproduksi cairan yang disebut *aqueous humor*. Cairan ini normalnya mengalir keluar melalui sudut pertemuan iris dan kornea. Jika saluran pembuangan ini tersumbat atau bekerja terlalu lambat, cairan menumpuk, menyebabkan tekanan di dalam bola mata meningkat dan merusak saraf optik secara perlahan.")
    
    st.subheader("Faktor Risiko")
    st.write("Beberapa faktor yang dapat meningkatkan risiko seseorang terkena glaukoma meliputi:")
    st.markdown("- **Tekanan bola mata tinggi:** Individu dengan Tekanan Intraokular (TIO) di atas batas normal.\n- **Usia di atas 40 tahun:** Risiko meningkat seiring bertambahnya usia.\n- **Riwayat keluarga (Genetik):** Memiliki anggota keluarga langsung (orang tua atau saudara kandung) dengan riwayat glaukoma.\n- **Anatomi mata:** Memiliki kornea yang tipis di bagian tengah atau rabun jauh/dekat yang ekstrem.\n- **Kondisi medis penyerta:** Menderita diabetes, migrain, sirkulasi darah buruk, atau tekanan darah tinggi/rendah yang tidak terkontrol.\n- **Penggunaan obat tetes mata kortikosteroid** dalam jangka waktu yang sangat panjang.")

    st.subheader("Gejala Glaukoma")
    st.write("Glaukoma dibedakan menjadi beberapa jenis dengan gejala yang berbeda:")
    st.markdown("- **Glaukoma Sudut Terbuka (Open-Angle):** Sering disebut sebagai *'pencuri penglihatan diam-diam'*. Tidak ada gejala pada tahap awal. Pada tahap lanjut, terjadi kehilangan penglihatan tepi (samping) hingga akhirnya seperti melihat melalui terowongan (*tunnel vision*).\n- **Glaukoma Sudut Tertutup Akut:** Muncul mendadak dan merupakan gawat darurat medis. Gejalanya meliputi nyeri mata yang hebat, sakit kepala, mual dan muntah, pandangan kabur seketika, dan melihat lingkaran cahaya (halo) di sekitar lampu.")

    st.info("💡 **Penanganan medis:** Kerusakan akibat glaukoma tidak dapat dikembalikan, tetapi dapat dihentikan agar tidak memburuk. Penanganan meliputi penggunaan obat tetes mata seumur hidup untuk menurunkan tekanan, terapi laser (Trabeculoplasty), hingga tindakan bedah pembedahan untuk membuat saluran drainase baru.")

with tab4:
    st.header("Kondisi Mata Normal (Sehat)")
    st.write("**Deskripsi:** Kondisi anatomi dan fisiologi mata yang berfungsi secara optimal. Pada mata normal, kornea dan lensa bening (tidak ada kekeruhan), tekanan cairan di dalam mata seimbang, saraf optik sehat, dan sistem pembuluh darah retina mengalirkan nutrisi tanpa adanya penyumbatan atau kebocoran.")
    
    st.subheader("Indikator Kesehatan Mata")
    st.markdown("- Ketajaman visual berada pada tingkat optimal (biasanya 20/20 atau 6/6).\n- Lapang pandang (penglihatan tepi) utuh tanpa *blind spot* yang tidak wajar.\n- Tekanan Intraokular (TIO) berada dalam rentang normal (umumnya 10 hingga 21 mmHg).\n- Kemampuan untuk memfokuskan objek pada jarak dekat dan jauh berfungsi dengan baik (akomodasi).")

    st.success("✅ **Panduan Pencegahan & Perawatan Mata Secara Medis:**")
    st.markdown("""
    1. **Pemeriksaan Mata Rutin (Screening):** Lakukan *General Eye Check-up* minimal 1-2 tahun sekali, terutama bagi mereka yang berusia di atas 40 tahun atau memiliki riwayat penyakit sistemik (seperti diabetes/hipertensi).
    2. **Terapkan Aturan 20-20-20:** Untuk mencegah *Digital Eye Strain* (mata lelah akibat gadget), setiap 20 menit menatap layar, istirahatkan mata dengan melihat objek sejauh 20 kaki (sekitar 6 meter) selama minimal 20 detik.
    3. **Nutrisi yang Tepat:** Konsumsi makanan yang kaya akan Lutein, Zeaxanthin, Vitamin C, Vitamin E, dan Asam Lemak Omega-3 (seperti sayuran hijau gelap, wortel, dan ikan salmon) yang terbukti secara klinis menjaga kesehatan makula retina.
    4. **Perlindungan Sinar UV:** Selalu gunakan kacamata hitam dengan proteksi 100% UVA/UVB saat berada di luar ruangan untuk mencegah pembentukan katarak dini dan kerusakan retina.
    5. **Gunakan APD Mata:** Pakai kacamata pelindung *safety* saat bekerja di area berisiko (bahan kimia, material tajam, atau pengelasan) untuk mencegah trauma mata.
    """)