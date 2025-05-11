import numpy as np
from sentence_transformers import SentenceTransformer
from logger import logging


def word_2_vec(text):
    model = SentenceTransformer('./artifacts/all-MiniLM-L6-v2')
    embeddings = model.encode(text)
    return embeddings


def distance(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.linalg.norm(a - b)


if __name__=="__main__":
    a = "tell me how much did I spend in the month of october"
    b1 = "expense spend cost price charge payment figure fee"
    b2 = "bill invoice statement account"
    b3 = "income earning salary remuneration wage stipend revenu taking profit gains turnover yield"
    dist1 = distance(word_2_vec(a), word_2_vec(b1))
    dist2 = distance(word_2_vec(a), word_2_vec(b2))
    dist3 = distance(word_2_vec(a), word_2_vec(b3))
    print(dist1, dist2, dist3)
