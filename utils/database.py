import sqlite3
import pandas as pd
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "history.db"

def init_db():
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
    init_db() 
    
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
    init_db() 
    conn = sqlite3.connect(DB_PATH)
    try:
        df = pd.read_sql_query("SELECT tanggal, hasil_prediksi, confidence FROM history ORDER BY tanggal DESC", conn)
    except Exception as e:
        df = pd.DataFrame(columns=["tanggal", "hasil_prediksi", "confidence"])
    finally:
        conn.close()
    return df
init_db()