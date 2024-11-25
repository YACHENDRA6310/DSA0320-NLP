from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
documents = [
    "The sky is blue and beautiful.",
    "Love this blue and bright sky!",
    "The quick brown fox jumps over the lazy dog.",
    "The brown fox is quick and the blue dog is lazy!"
]
query = "blue sky"
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
query_vector = vectorizer.transform([query])
cosine_similarities = (tfidf_matrix @ query_vector.T).toarray()
ranked_indices = np.argsort(cosine_similarities.flatten())[::-1]
print("Document Rankings:")
for rank, index in enumerate(ranked_indices, start=1):
    print(f"Rank {rank}: Document {index+1} - Score: {cosine_similarities[index][0]:.4f}")
