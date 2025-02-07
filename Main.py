import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from fastapi import FastAPI

# Predefined passages (static data)
book_text = [
    "John is a detective solving crimes.",
    "The city has flying cars.",
    "The detective investigates mysterious events every night.",
    "In the future, robots assist humans with daily tasks."
]

# Predefined questions (static data)
questions = [
    "What is the occupation of John?",
    "What technology exists in the city?",
    "What is the detective's main job?",
    "How do robots help humans?"
]

# Load retrieval model
retrieval_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Initialize FAISS index with the correct dimension (384 for all-MiniLM-L6-v2)
index = faiss.IndexFlatL2(384)  # Correct dimensionality is 384

# Encode the book text and add to FAISS index
embeddings = retrieval_model.encode(book_text)

# Convert embeddings to numpy array and ensure they are of type float32
embeddings = np.array(embeddings).astype('float32')

# Now add the embeddings to the FAISS index
try:
    index.add(embeddings)
    print("Embeddings added to FAISS index successfully.")
except Exception as e:
    print(f"Error adding embeddings to FAISS index: {e}")

# FastAPI app
app = FastAPI()

@app.get("/ask")
def answer_question(question: str):
    # Ensure the question is in the predefined list of questions
    if question not in questions:
        return {"error": "This question is not predefined."}
    
    # Encode the question and find the closest passage
    question_embedding = retrieval_model.encode([question])[0]
    _, idx = index.search(np.array([question_embedding]), k=1)
    retrieved_text = book_text[idx[0][0]]
    
    return {"retrieved_passage": retrieved_text}
