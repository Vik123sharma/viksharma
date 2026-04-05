import streamlit as st
from pdf2docx import Converter
import os

# --- CONFIGURATION ---
USER_PASSWORD = "MySecretPassword123" # <--- Yahan apna pasandida password rakho

st.set_page_config(page_title="Vikash's PDF Converter", layout="centered")

# --- LOGIN SYSTEM ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.title("🔒 Private PDF Converter")
    pwd = st.text_input("Enter Password to Access", type="password")
    if st.button("Login"):
        if pwd == USER_PASSWORD:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Galat Password! Dubara koshish karein.")
else:
    # --- MAIN APP INTERFACE ---
    st.title("📄 PDF to DOCX Professional Converter")
    st.write("Upload heavy PDF files (Up to 200-300 pages)")

    uploaded_file = st.file_input("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        if st.button("Convert Now"):
            with st.spinner("Converting... Isme thoda samay lag sakta hai, kripya wait karein."):
                try:
                    docx_file = "converted_result.docx"
                    cv = Converter("temp.pdf")
                    # Memory bachane ke liye hum saare pages ek saath convert karenge
                    cv.convert(docx_file, start=0, end=None)
                    cv.close()

                    with open(docx_file, "rb") as f:
                        st.download_button(
                            label="📥 Download Word File",
                            data=f,
                            file_name=uploaded_file.name.replace(".pdf", ".docx"),
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                        )
                    st.success("Conversion Successful!")
                except Exception as e:
                    st.error(f"Error: {e}")
                finally:
                    if os.path.exists("temp.pdf"): os.remove("temp.pdf")