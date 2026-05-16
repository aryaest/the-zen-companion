import streamlit as st
import google.generativeai as genai
import os

# 1. Setup Konfigurasi Halaman
st.set_page_config(
    page_title="The Zen Companion",
    page_icon="🧘",
    layout="centered"
)

# 2. Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stTextArea>div>div>textarea {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Profil The Fit Coder)
with st.sidebar:
    st.title("👨‍💻 The Fit Coder")
    st.info("Merging Informatics Excellence with Physical Discipline.")
    st.markdown("---")
    st.write("**Tech Stack:**")
    st.code("Python\nStreamlit\nGemini 2.5 Flash")
    st.markdown("---")
    st.caption("Build for #JuaraVibeCoding")

# 4. Bagian UI Utama
st.title("🧘 Wellness: The Zen Companion")
st.markdown("### Harmonisasi Logika, Fisik, dan Mindset")
st.write("Ceritakan kondisimu (tugas kuliah, progres coding, atau kondisi fisik)...")

user_input = st.text_area("Apa yang sedang dirasakan?", 
                         placeholder="Contoh: Otak panas karena bug, tapi jadwal hari ini harusnya disertai dengan olahraga dan meditasi...",
                         height=150)

if st.button("Dapatkan Bimbingan Zen"):
    if user_input:
        with st.spinner("Menyelaraskan pikiran dan energi..."):
            try:
                # API Key
                api_key = os.environ.get("GEMINI_API_KEY")
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('models/gemini-2.5-flash')
                
                # Prompt tanpa nama (Universal Mentor)
                prompt = f"""
                Kamu adalah 'The Zen Companion', seorang mentor elit yang ahli dalam Stoikisme, 
                fitness, dan programming. 

                User sedang berkonsultasi tentang ini: '{user_input}'
                
                Berikan respon terstruktur tanpa menyebut nama user:
                1. Analisis Energi: Analisis kondisi mental & fisik user saat ini secara tajam.
                2. Modifikasi Aktivitas: Apa yang sebaiknya dilakukan (latihan/coding) agar tetap disiplin tapi bijak?
                3. Stoic Wisdom: Satu kutipan filosofi Stoik yang sangat relevan dengan situasi ini.
                
                Gunakan nada bicara yang tenang, maskulin, berwibawa, dan mendukung. 
                Jangan gunakan sapaan nama dalam respon.
                """
                
                response = model.generate_content(prompt)
                
                st.success("Analisis Selesai!")
                st.markdown("---")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Terjadi kesalahan teknis: {e}")
    else:
        st.warning("Ceritakan kondisimu terlebih dahulu.")
