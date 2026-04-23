import streamlit as st

def apply_modern_sidebar():
    st.markdown("""
    <style>
    /* Mengubah latar belakang sidebar dengan gradient hitam ke hijau gelap */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #091413 0%, #0d1f1c 100%);
        border-right: 1px solid #1a332d;
    }

    /* Memberi ruang ekstra di bagian atas untuk Header buatan kita */
    [data-testid="stSidebarNav"] {
        padding-top: 110px; 
    }

    /* --- STYLING ITEM MENU --- */
    [data-testid="stSidebarNav"] a {
        margin: 8px 20px;
        padding: 12px 15px !important;
        border-radius: 12px;
        transition: all 0.3s ease;
        color: #9ca3af !important;
        font-weight: 500;
    }

    /* Efek Hover (Saat kursor mouse mendekat) */
    [data-testid="stSidebarNav"] a:hover {
        background-color: rgba(64, 138, 113, 0.15) !important;
        transform: translateX(8px); /* Efek bergeser modern */
        color: #ffffff !important;
    }

    /* Efek Active (Halaman yang sedang dibuka saat ini) */
    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background-color: #408a71 !important;
        color: white !important;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(64, 138, 113, 0.4); /* Efek bersinar / glow */
    }
    </style>
    """, unsafe_allow_html=True)


    with st.sidebar:
        st.markdown("""
        """, unsafe_allow_html=True)