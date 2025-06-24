import streamlit as st
from pathlib import Path
from process_data import extract_text
from semantic import semantic_sections
from structure_metadata import generate_metadata

st.title("Automated Document Metadata Generator")

uploaded_file = st.file_uploader("Upload a document (.txt, .docx, .pdf)", type=["txt", "docx", "pdf"])

if uploaded_file is not None:
    temp_path = Path("temp_" + uploaded_file.name)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File uploaded: {uploaded_file.name}")

    if st.button("Generate Metadata"):
        with st.spinner("Analyzing document..."):
            metadata = generate_metadata(str(temp_path))
        st.subheader("Generated Metadata")
        st.json(metadata)
else:
    st.info("Please upload a file to get started.")
