# 📄 Automated Metadata Generator

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.34.0+-FF4B4B)](https://streamlit.io/)

**Automatically extract, analyze, and generate rich metadata from your documents!**

---

## ✨ Features

- **Supports Multiple Formats:** Upload `.txt`, `.docx`, or `.pdf` files.
- **Text Extraction:** Uses advanced OCR (EasyOCR) and AI-powered parsing (LlamaParse) for robust text extraction.
- **Semantic Analysis:** Identifies key sentences and sections using NLP and sentence embeddings.
- **Metadata Generation:** Produces comprehensive metadata including:
  - File info (name, timestamp)
  - Document stats (length, word count, reading time)
  - Language detection
  - Named entity recognition (people, organizations, locations, etc.)
  - Semantic summary of top sections

---

---

## 🛠️ Technologies Used

| Technology      | Purpose                                             |
|-----------------|-----------------------------------------------------|
| **Streamlit**   | Interactive web app framework                       |
| **EasyOCR**     | OCR for extracting text from scanned PDFs           |
| **LlamaParse**  | AI-powered document parsing                         |
| **spaCy**       | NLP for entity recognition and sentence splitting   |
| **NLTK**        | Text processing and tokenization                    |
| **SentenceTransformers** | Embedding models for semantic analysis      |
| **langdetect**  | Language detection                                  |
| **pytz**        | Timezone handling                                   |

---
# 🤖 Intelligent Document Metadata Generator

Welcome to the **Automated Document Metadata Generator**, an AI-powered Streamlit application that extracts, analyzes, and generates rich metadata from any document.

---

## 🤖 Intelligent Text Processing

- **Dual Extraction Engine**  
  Combines LlamaParse AI parsing with EasyOCR for maximum text recovery.

- **Smart OCR**  
  Handles scanned documents and image-based PDFs seamlessly.

- **Language Detection**  
  Automatically identifies the document’s language.

- **Named Entity Recognition**  
  Extracts people, organizations, locations, and more.

---

## 📊 Comprehensive Metadata Generation

- **Document Statistics**  
  Word count, paragraph count, and reading-time estimation.

- **Semantic Analysis**  
  Identifies key sentences and document sections using sentence embeddings.

- **Entity Mapping**  
  Categorizes and organizes all named entities.

- **Timestamp Tracking**  
  Records processing time with full timezone support.

---

## 🌐 Live Application

The app is deployed and accessible at:  
**https://automated-meta-data-generator-nfri5jph5uqyxaypx4xsst.streamlit.app**

---

## 🔧 Advanced Features

### Semantic Analysis Engine  
- **Sentence Embeddings**  
  Uses the all-MiniLM-L6-v2 model for deep semantic understanding.  
- **Cosine Similarity**  
  Ranks sections by representativeness.  
- **Automatic Summarization**  
  Extracts the top five key sentences as a concise summary.

### Entity Recognition System  
- **Multi-category Classification**  
  Supports PERSON, ORG, GPE, DATE, and more.  
- **Confidence Scoring**  
  Ranks entities by relevance and frequency.  
- **Duplicate Handling**  
  Performs intelligent deduplication and normalization.

---

## 🎯 Use Cases

- **Document Management**  
  Automatically catalog and organize large document libraries.  
- **Content Analysis**  
  Extract insights from research papers, reports, and whitepapers.  
- **Legal Discovery**  
  Process legal documents for entity identification and case insights.  
- **Academic Research**  
  Analyze scholarly articles and extract key findings.  
- **Business Intelligence**  
  Parse contracts, invoices, and business documents for actionable data.

---

## 🔮 Future Enhancements

- **Batch Processing**  
  Support for multiple file uploads and parallel processing.  
- **Custom Entity Types**  
  Allow users to define their own categories and labels.  
- **Export Formats**  
  CSV, Excel, and XML output options for downstream tools.  
- **Advanced Analytics**  
  Document similarity, clustering, and topic modeling.  
- **Multi-language Support**  
  Enhanced detection and processing for non-English documents.

---

## 💡 Usage Example

1. **Upload a document** (.txt, .docx, or .pdf).
2. **Click "Generate Metadata"**.
3. **View the generated metadata** in JSON format.

---




