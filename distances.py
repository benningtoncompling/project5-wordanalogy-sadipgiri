'''
    Python3 program to calculate different distances between two vectors
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 10th May, 2019
'''

import numpy as np

def euclidean_dist(vector_1, vector_2):
    '''
        Euclidean distance or Euclidean metric is the "ordinary" straight-line distance between two points in Euclidean space. 
        With this distance, Euclidean space becomes a metric space. The associated norm is called the Euclidean norm.
        Euclidean distance is also known as L2 norm.

        Optimization Options (for faster calculation):
            1. don't need to calculate square root since we can compare between squares
            2. instead of squaring: use vector transpose operator:
                -> euclidean_distance(x, y) = (x − y)T (x − y) where, T is transpose
    '''

    # initial distance calculation:
    # return np.sqrt(np.sum(np.square(vector_1 - vector_2)))

    # use vector transpose operator: (x − y)T (x − y) where, T is transpose
    # return np.dot(np.transpose(vector_1 - vector_2), vector_1 - vector_2)

    # just using sum of squares between vectors
    return np.sum(np.square(vector_1 - vector_2))

def manhattan_dist(vector_1, vector_2):
    '''
        The Manhattan distance, also known as Levenshtein distance or L1 norm, is ∑ |xi − yi|
    '''
    return np.sum(np.abs(vector_2 - vector_1))

def cosine_dist(vector_1, vector_2):
    '''
        Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space that measures the cosine of the angle between them.
        Mathematically, it's dot product between two vectors.
    '''
    return np.dot(vector_1, vector_2)

if __name__ == '__main__':
    v1 = np.array([i for i in range(100) if i % 2 == 0])
    v2 = np.array([i for i in range(100) if i % 2 != 0])
    print(euclidean_dist(v1,v2))
    print(manhattan_dist(v1, v2))
    