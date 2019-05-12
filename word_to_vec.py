'''
    Python3 program to read vectors of all words
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 11th May 2019
'''

import numpy as np

def word_to_vec_dict(model_file):
    ''' 
        Task: read all words to vectors
        Approach: 
            1. create a dictionary
            2. make each word a key and their values' a numpy array (technically; a vector)
            [details: lower case all words for consistency, no duplicate words, vector element's type -> a float]
    '''
    dct = {}
    with open(model_file, 'r') as file:
        lines = file.read().splitlines()
    for line in lines:
        temp_list = line.split()
        word = temp_list[0].lower()
        word_vec = np.array(temp_list[1:]).astype('float')
        if word not in dct:
            dct[word] = word_vec
    return dct

def normalize_word_to_vec(model_file):
    '''
        Task: 
            normalize word to vector dictionary i.e. convert vector to its unit vector
        Approach:
            Same as defined above but with normalized vector
            Formulae: vec/mag(vec)
                where, mag(vec) is the square root of sum of squares of the vector
            Could use numpy for faster arithmic!
        [NOTE: could have normalized above dict but for faster arithmmic directly making a normalized dict (following typical instructions)]
    '''
    normalized_dct = {}
    with open(model_file, 'r') as file:
        lines = file.read().splitlines()
    for line in lines:
        temp_list = line.split()
        word = temp_list[0].lower()
        word_vec = np.array(temp_list[1:]).astype('float')
        if word not in normalized_dct:
            normalized_dct[word] = word_vec/np.sqrt(np.sum(np.square(word_vec)))
    return normalized_dct

if __name__ == '__main__':
    df = word_to_vec_dict('smaller_model.txt')
    df_norm = normalize_word_to_vec('vector_model_5_10.txt')
    print(df['rapidly'])
    print(df_norm['rapidly'])