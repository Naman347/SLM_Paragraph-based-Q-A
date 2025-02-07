Small Language Model (SLM) for Book-Based Question Answering 📖🤖

🚀 A lightweight and efficient language model for retrieving relevant passages from books and answering user queries.

🔹 Features

✅ Dynamic Passage Addition – Users can add book passages via API.✅ Fast & Accurate Retrieval – Uses FAISS indexing and MiniLM embeddings.✅ Ready-to-Use – No additional training required.✅ Scalable & Efficient – Handles large datasets with optimized search.

📌 How It Works

1️⃣ Users upload book passages via /add_passages API.2️⃣ The system encodes passages into vector embeddings.3️⃣ FAISS retrieves the most relevant passage for a given question.4️⃣ Returns the best-matching passage as the answer.

🔧 Installation & Setup

1. Clone the Repository

git clone https://github.com/your-repo/slm-book-qa.git
cd slm-book-qa

2. Install Dependencies

pip install -r requirements.txt

3. Run the API Server

uvicorn app:app --reload

📝 Usage

1. Add Book Passages

curl -X POST "http://127.0.0.1:8000/add_passages" -H "Content-Type: application/json" -d '{"passages": ["John is a detective solving crimes.", "The city has flying cars."]}'

2. Ask a Question

curl "http://127.0.0.1:8000/ask?question=Who is John?"

Expected Output

{"retrieved_passage": "John is a detective solving crimes."}

🛠 Technologies Used

SentenceTransformers (MiniLM) for text embeddings

FAISS for efficient passage retrieval

FastAPI for API handling

Python (NumPy, Torch)

📌 Key Learnings & Observations

✅ Efficient retrieval with FAISS improves query performance.✅ No fine-tuning required, making it lightweight and fast.✅ Highly scalable – Can handle thousands of book passages.

📎 Contributing

Want to contribute? Open an issue or submit a pull request!
