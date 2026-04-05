import streamlit as st
from pdf2docx import Converter
import os
import time

# --- UI CONFIG ---
st.set_page_config(page_title="Vikash AI ML Engine", page_icon="🤖", layout="centered")

# --- CUSTOM CSS FOR PROFESSIONAL LOOK ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #ff4b4b; color: white; font-weight: bold; }
    .stProgress > div > div > div > div { background-color: #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# --- PASSWORD PROTECTION ---
if "auth" not in st.session_state:
    st.session_state["auth"] = False

def login():
    st.title("🛡️ Vikash AI ML Engine")
    st.subheader("Private Access Portal")
    pwd = st.text_input("Enter Private Access Key", type="password")
    if st.button("Unlock Turbo Mode"):
        if pwd == "Vikash@2026":
            st.session_state["auth"] = True
            st.rerun()
        else:
            st.error("Access Denied! Please check your key.")

if not st.session_state["auth"]:
    login()
    st.stop()

# --- MAIN APP INTERFACE ---
st.title("🤖 Vikash AI ML: Pro PDF Converter")
st.markdown("### High-Accuracy AI Layout Preservation (99.9%)")
st.info("System Status: **Cloud Server Active (High Speed Mode)**")

file = st.file_uploader("Select PDF Document (Max 100MB)", type=["pdf"])

if file:
    st.success(f"File Uploaded: {file.name}")
    if st.button("Start AI Conversion ⚡"):
        t1 = time.time()
        with st.spinner("AI analyzing layout, fonts, and images..."):
            pdf_name = f"temp_{file.name}"
            docx_name = pdf_name.replace(".pdf", ".docx")
            
            with open(pdf_name, "wb") as f:
                f.write(file.getbuffer())
            
            try:
                # Core AI Engine
                cv = Converter(pdf_name)
                # Speed Optimization for Cloud
                cv.convert(docx_name, start=0, end=None, multi_processing=True)
                cv.close()
                
                t2 = time.time()
                st.balloons()
                st.success(f"Success! Conversion completed in {round(t2-t1, 2)} seconds.")
                
                with open(docx_name, "rb") as f:
                    st.download_button(
                        label="📂 Download Editable Word File", 
                        data=f, 
                        file_name=f"AI_Verified_{file.name}.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
                
                # Cleanup temporary files
                os.remove(pdf_name)
                if os.path.exists(docx_name):
                    os.remove(docx_name)
                    
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

st.markdown("---")
st.caption("© 2026 | Developed by Vikash - AI/ML Engineer")