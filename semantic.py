import nltk
import spacy
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)

nlp = spacy.load('en_core_web_sm')
sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
def semantic_sections(raw_text: str, top_n: int = 5) -> list[str]:
    sentences = [
        sent.text.strip()
        for sent in nlp(raw_text).sents
        if len(sent.text.strip()) > 20
    ]
    embeddings = sentence_model.encode(sentences)
    avg_embedding = embeddings.mean(axis=0, keepdims=True)
    similarities = cosine_similarity(embeddings, avg_embedding).flatten()
    top_indices = similarities.argsort()[-top_n:][::-1]
    return [sentences[i] for i in top_indices]
