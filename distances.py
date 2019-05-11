import numpy as np

def euclidean_dist(vector_1, vector_2):
    return np.sqrt(np.sum(np.square(vector_1 - vector_2)))

def manhattan_dist(vector_1, vector_2):
    return np.sum(np.abs(vector_2 - vector_1))

def cosine_dist(vector_1, vector_2):
    return np.dot(vector_1, vector_2)
    