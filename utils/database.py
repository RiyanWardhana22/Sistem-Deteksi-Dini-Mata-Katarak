import sqlite3
import pandas as pd
from datetime import datetime
from pathlib import Path

# Setup Path Database secara dinamis
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "history.db"

def init_db():
    """Membuat tabel riwayat jika belum ada."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tanggal TEXT,
            hasil_prediksi TEXT,
            confidence REAL,
            image_path TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_prediction(hasil, confidence, image_name):
    """Menyimpan hasil analisis ke database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO history (tanggal, hasil_prediksi, confidence, image_path)
        VALUES (?, ?, ?, ?)
    ''', (tanggal, hasil, confidence, image_name))
    conn.commit()
    conn.close()

def get_history():
    """Mengambil semua data riwayat dalam bentuk DataFrame Pandas."""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT tanggal, hasil_prediksi, confidence FROM history ORDER BY tanggal DESC", conn)
    conn.close()
    return df