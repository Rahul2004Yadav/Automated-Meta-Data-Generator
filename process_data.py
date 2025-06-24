from pathlib import Path
from docx import Document
import fitz  
from PIL import Image
import numpy as np
import easyocr
from llama_parse import LlamaParse
import os

reader = easyocr.Reader(['en'])
from dotenv import load_dotenv
load_dotenv()
parser = LlamaParse(api_key=os.environ.get('LLAMA_PARSE_API_KEY'), result_type="text")
#extract using llamaparse& easyocr
def extract_text(path: str) -> str:
    ext = path.lower().split('.')[-1]
    if ext == 'txt':
        return Path(path).read_text(encoding='utf-8')
    elif ext == 'docx':
        return "\n".join(p.text for p in Document(path).paragraphs)
    elif ext == 'pdf':
        llama_text = ""
        ocr_text = ""
        try:
            parsed = parser.load_data(path)
            if parsed:
                llama_text = str(parsed[0].text)
        except Exception as e:
            print(f"LlamaParse had issues: {e}")
        doc = fitz.open(path)
        for page in doc:
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), colorspace=fitz.csRGB)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            page_ocr = reader.readtext(np.array(img), detail=0, paragraph=True)
            ocr_text += "\n".join(str(s) for s in page_ocr) + "\n"       
        # Combine both results
        combined_text = f"{llama_text}\n\n--- OCR Content ---\n{ocr_text}".strip()
        return combined_text if combined_text else "No text found" 
    
