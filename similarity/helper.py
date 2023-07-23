from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import random


def calculate_similarity(search_input: str, item_dict: dict) -> list:
    items_list = []

    for k, v in item_dict.items():
        items_list.append(v)
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform([search_input] + items_list)
    cosine_similarities = linear_kernel(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    cosine_similarities_indexes = [index + 1 for index, value in enumerate(cosine_similarities) if value > 0.18]
    return cosine_similarities_indexes


if __name__ == '__main__':
    d = {1: 'this is a description number one 1', 2: 'This is from postman request', 3: 'This is from postman request'}
    b = calculate_similarity('postman', d)
    print(b)
