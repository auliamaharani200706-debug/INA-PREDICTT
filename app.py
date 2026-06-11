import streamlit as st
import os
import pathlib

st.set_page_config(
    page_title="INA-PREDICT | Early Warning System",
    page_icon="🌋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Dapatkan direktori tempat file app.py berada
BASE_DIR = pathlib.Path(__file__).parent.absolute()

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppHeader {display: none;}
    .main .block-container { padding: 0 !important; max-width: 100% !important; }
    iframe { width: 100%; height: calc(100vh - 0px); border: none; margin: 0; padding: 0; }
    .stAppDeployButton { display: none; }
</style>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "📋 Pilih Menu",
    ["Dashboard", "Prediksi Bencana", "Panduan Aksi", "Kontak Darurat", "Donasi", "Hubungi Kami"],
    index=0
)

html_files = {
    "Dashboard": "index.html",
    "Prediksi Bencana": "prediksi.html",
    "Panduan Aksi": "panduan.html",
    "Kontak Darurat": "kontak.html",
    "Donasi": "donasi.html",
    "Hubungi Kami": "hubungikami.html"
}

def load_html(filename):
    filepath = BASE_DIR / filename
    if filepath.exists():
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return f"""
        <!DOCTYPE html>
        <html>
        <head><meta charset="UTF-8"><title>Error</title></head>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>❌ File Tidak Ditemukan</h1>
            <p>File {filename} tidak ditemukan di {BASE_DIR}</p>
            <p>File yang tersedia: {list(BASE_DIR.glob('*.html'))}</p>
        </body>
        </html>
        """

st.components.v1.html(load_html(html_files[page]), height=850, scrolling=True)

st.sidebar.markdown("---")
st.sidebar.caption("© 2026 INA-PREDICT")
st.sidebar.caption("Early Warning System Indonesia")