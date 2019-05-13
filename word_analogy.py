#!/usr/bin/env python3

'''
    Word analogy python3 program -> that solves analogies such as "dog is to cat as puppy is to ___".
    Author: Sadip Giri (sadipgiri@bennington.edu)
    Date: 10th May, 2019
'''

import numpy as np
import os
import sys
from distances import euclidean_dist, manhattan_dist, cosine_dist
from word_to_vec import word_to_vec_dict, normalize_word_to_vec

words_vector_file = sys.argv[1]
input_directory = sys.argv[2]
output_directory = sys.argv[3]
evaluation_file = sys.argv[4]
should_normalize = int(sys.argv[5])
similarity_type = int(sys.argv[6])

# dynamic programming approach:
if should_normalize == 1:
    dataframe = normalize_word_to_vec(words_vector_file)
else:
    dataframe = word_to_vec_dict(words_vector_file)

def compare_and_return_fourth_vector(word1,word2,word3, similarity_type):
    '''
        Task: return fourth word using word analogy of given other three words
        Approach:
            1. calculate fourth vector: vec4 = vec3 + vec2 - vec1
            2. Depending on the similarity types such as 
                - Euclidean Distance (L1 norm)
                - Manhattan Distance (L2 norm)
                - Cosine Distance (Dot Product)
                - Average of all three similarities
                find the smallest distance vector and its word.
            [Some of the details are commented within each functionalities/roadblocks]

            OPTIMIZATION:
            - compare if fourth word is not all other three words
            - 
    '''
    #lower case all words before checking!
    word1 = word1.lower()
    word2 = word2.lower()
    word3 = word3.lower()
    # if the word's vector exists or not?
    if (word1 not in dataframe.keys()) or (word2 not in dataframe.keys()) or (word3 not in dataframe.keys()):
        return 'none'
    v1=dataframe[word1]
    v2=dataframe[word2]
    v3=dataframe[word3]
    predicted_vect = v3 + v2 - v1 # gettting predicted 4th vector
    # Distances/Similarities Cases:
    if similarity_type == 0:
        '''
            euclidean distance comparison
        '''
        initial_dist = euclidean_dist(vector_1=predicted_vect, vector_2=dataframe[list(dataframe.keys())[0]]) # initialise
        word = list(dataframe.keys())[0]
        for i in dataframe:
            if i not in [word1, word2, word3]: # so that it won't predict same words Ha!
                temp_euclidean_dist = euclidean_dist(vector_1=predicted_vect,vector_2=dataframe[i])
                if temp_euclidean_dist < initial_dist:
                    word = i
                    initial_dist = temp_euclidean_dist
        return word
    
    if similarity_type == 1:
        '''
            manhattan distance comparison
        '''
        initial_dist = manhattan_dist(vector_1=predicted_vect, vector_2=dataframe[list(dataframe.keys())[0]]) # initialise
        word = list(dataframe.keys())[0]
        for i in dataframe:
            if i not in [word1, word2, word3]: 
                temp_manhattan_dist = manhattan_dist(vector_1=predicted_vect,vector_2=dataframe[i])
                if temp_manhattan_dist < initial_dist:
                    word = i
                    initial_dist = temp_manhattan_dist
        return word
    
    if similarity_type == 2:
        '''
            cosine distance comparison
            NOTE: cosine is other way around so needs to check if its larger in our implementation
                or we'd subtract by 1 to do it the same way as L1, L2, etc distances way
        '''
        initial_dist = cosine_dist(vector_1=predicted_vect, vector_2=dataframe[list(dataframe.keys())[0]], normalized=should_normalize) # initialise
        word = list(dataframe.keys())[0]
        for i in dataframe:
            if i not in [word1, word2, word3]:
                temp_cosine_dist = cosine_dist(vector_1=predicted_vect,vector_2=dataframe[i], normalized=should_normalize)
                if temp_cosine_dist > initial_dist: # cosine comparison is other way around!
                    word = i
                    initial_dist = temp_cosine_dist
        return word
    
    if similarity_type == 3:
        '''
            average of all distances comparison
        '''
        initial_avg_dist = (euclidean_dist(vector_1=predicted_vect, vector_2=dataframe[list(dataframe.keys())[0]]) + manhattan_dist(vector_1=predicted_vect, vector_2=dataframe[list(dataframe.keys())[0]]) + (1-cosine_dist(vector_1=predicted_vect, vector_2=dataframe[list(dataframe.keys())[0]], normalized=should_normalize)))/3 # initialise
        word = list(dataframe.keys())[0]
        for i in dataframe:
            if i not in [word1, word2, word3]:
                temp_avg_dist = (euclidean_dist(vector_1=predicted_vect, vector_2=dataframe[i]) + manhattan_dist(vector_1=predicted_vect, vector_2=dataframe[i]) + (1-cosine_dist(vector_1=predicted_vect, vector_2=dataframe[i], normalized=should_normalize)))/3
                if temp_avg_dist < initial_avg_dist:
                    word = i
                    initial_avg_dist = temp_avg_dist
        return word

def read_write_format(input_dir, output_dir, evaluation_file, similarity_type):
    '''
        Task:
            - Create new analogy test files out of input_test (GoogleTestFile)
                - including evaluation file within it (accuracy of each file; plus, total accuracy!)
            - Depending on the given arguments (implement or not below methods):
                - Normalization
                - Similarity types: 0(Euclidean Distance), 1(Manhattan Distance), 2(Cosine Distance), 3(Avg Distance)
        
        Approach:
            - List all test files (only .txt) e.g. .txt files in GoogleTestFile
            - Loop through all words (2 pairs/4 wrods) and compare 4 test word with fourth predicted word 
            - Finally write fourth predicted words in all new Output file for each test files
                - depending on given similarity type and normalization
            - At the same time, write evaluation files in each output dir according to given format
                - including: accuracy of each file and total accuracy of that output dir type.
    '''
    # track total accuracy:
    total_correct_guesses = 0
    total_guesses = 0
    # to finally write evaluation file:
    eval_write_format = []
    # list all .txt files from given input test dir e.g. GoogleTestFile
    input_files = [file for file in os.listdir(input_dir) if file.endswith('.txt')]
    for file in input_files:
        print('Loading: {0}'.format(file))
        # to track accuracy of each file
        temp_correctly_guessed =  0
        temp_write_format = []
        # read each file's lines
        with open('{0}/{1}'.format(input_dir, file), 'r') as f:
            lines = f.read().splitlines()
        temp_total_words = len(lines)
        # for each line with 4 words: find predicted fourth word and compare with existing 4th word
            # -> using above compare function
        for line in lines:
            words = line.split()
            fourth_word = compare_and_return_fourth_vector(words[0], words[1], words[2],similarity_type)
            if fourth_word == words[3].lower():
                temp_correctly_guessed += 1
            temp_write_format.append(' '.join(words[:3] + [fourth_word + '\n'])) # could use .capitlize() to follow case consistency!!
        # finally, write 3 words + 4th predicted word in output dir epecified
        with open('{0}/{1}'.format(output_dir,file), 'w') as write_file:
            write_file.write(''.join(temp_write_format))
        print('Done: {0}'.format(file))
        eval_write_format.append(file + '\n')
        eval_write_format.append('ACCURACY: {0}% ({1}/{2})\n'.format(temp_correctly_guessed/temp_total_words * 100, temp_correctly_guessed, temp_total_words))
        total_correct_guesses += temp_correctly_guessed
        total_guesses += temp_total_words
    # finally include total accuracy in evaluation file:
    eval_write_format.append('Total accuracy: {0}% ({1}/{2})'.format(total_correct_guesses/total_guesses * 100, total_correct_guesses, total_guesses))
    with open(evaluation_file, 'w') as eval_file:
        eval_file.write(''.join(eval_write_format))
    return 'Hurray Done!'

# finally: execute everything at once:
read_write_format(input_directory, output_directory, evaluation_file, similarity_type)