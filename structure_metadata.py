from pathlib import Path
from datetime import datetime
from collections import defaultdict
from langdetect import detect
import pytz
import spacy

from process_data import extract_text
from semantic import semantic_sections
nlp = spacy.load("en_core_web_sm")
def generate_metadata(path: str) -> dict:
    p = Path(path)
    try:
        text = extract_text(str(p))
        entities_map = defaultdict(set)
        for ent in nlp(text).ents:
            entities_map[ent.label_].add(ent.text)
        entities = {label: sorted(list(vals)) for label, vals in entities_map.items()}
        dominant_entity = max(entities.items(), key=lambda x: len(x[1]))[0] if entities else "N/A"     
        # Content analysis
        paragraphs = [p for p in text.split('\n') if p.strip()]
        word_count = len(text.split())
        reading_time = word_count // 200 + 1      
        # Semantic summary
        summary = []
        for i, sec in enumerate(semantic_sections(text), 1):
            snippet = str(sec).strip().replace("\n", " ")
            if len(snippet) > 400:
                snippet = snippet[:197].rsplit(" ", 1)[0] + " ..."
            summary.append(f"{i}. {snippet}")       
        # Structured metadata
        metadata = {
            "filename": p.name,
            "timestamp": datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S IST'),
            "document_length": len(text),
            "word_count": word_count,
            "reading_time_min": reading_time,
            "paragraph_count": len(paragraphs),
            "language": detect(text),
            "dominant_entity_type": dominant_entity,
            "summary_sections": summary,
            "named_entities": entities
        }
        return metadata       
    except Exception as e:
        return {"error": f"Error processing {p.name}: {str(e)}"}

