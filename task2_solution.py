from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Define documents and query
documents = [
    "Machine learning algorithms analyze structured data effectively",
    "Deep learning and neural networks excel at processing unstructured data",
    "Natural language processing helps computers understand human language",
    "Python is widely used for machine learning and data science"
]
query = ["machine learning algorithms for data"]

# 2. Fit CountVectorizer on documents and transform both documents and query
vectorizer = CountVectorizer()
doc_vectors = vectorizer.fit_transform(documents)
query_vector = vectorizer.transform(query)

# 3. Compute pairwise cosine similarity
similarity_scores = cosine_similarity(query_vector, doc_vectors).flatten()

# 4. Display ranked documents from highest score to lowest score
ranked_docs = sorted(
    list(enumerate(similarity_scores)), key=lambda x: x[1], reverse=True
)

print("Ranked Documents:")
for idx, score in ranked_docs:
  print(f"Score: {score:.4f} | Document: {documents[idx]}")