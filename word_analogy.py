#!/usr/bin/env python3

#import pandas as pd
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

'''
# note: make its taking time because of pandas dataframe!! so if its not normalizing then just use dictionary???
dataframe = pd.read_csv(words_vector_file, delimiter=' ', header=None)
dataframe = dataframe.set_index(dataframe[0]).T
dataframe = dataframe[1:]
dataframe.columns = [i.lower() for i in dataframe.columns]
# Task: to eliminate duplicate columns!!
#dataframe = dataframe.loc[:,~dataframe.columns.duplicated()] # for duplicate columns from stack overflow: https://stackoverflow.com/questions/14984119/python-pandas-remove-duplicate-columns

if should_normalize == 1:
    # using this handy pandas faster normalization technique
    # i.e. it normalizes everything at once then compare distances!!
    # uses dynamiz programming approaches!
    dataframe = dataframe/(((dataframe**2).sum())**(1/2))
'''

if should_normalize == 1:
    dataframe = normalize_word_to_vec(words_vector_file)
else:
    dataframe = word_to_vec_dict(words_vector_file)

def compare_and_return_fourth_vector(word1,word2,word3, similarity_type):
    '''
    '''
    #lower case all words before checking!
    word1 = word1.lower()
    word2 = word2.lower()
    word3 = word3.lower()

    # if the word's vector exists or not?
    if (word1 not in dataframe.keys()) or (word2 not in dataframe.keys()) or (word3 not in dataframe.keys()):
        return 'none'
        
    # there might be problem with duplicate column names!
        # this'd be fixed deleting duplicate columns but might take time!!
    v1=dataframe[word1]
    v2=dataframe[word2]
    v3=dataframe[word3]
    
    predicted_vect = v3 + v2 - v1 # gettting predicted 4th vector
    if similarity_type == 0:
        '''
            euclidean distance comparison
        '''
        initial_dist = euclidean_dist(vector_1=predicted_vect, vector_2=dataframe[list(dataframe.keys())[0]]) # initilise
        word = list(dataframe.keys())[0]
        for i in dataframe:
            if i != word3: # so that it won't predict 3rd word haha!
                temp_euclidean_dist = euclidean_dist(vector_1=predicted_vect,vector_2=dataframe[i])
                if temp_euclidean_dist < initial_dist:
                    word = i
                    initial_dist = temp_euclidean_dist
        return word
    
    if similarity_type == 1:
        '''
            manhattan distance comparison
        '''
        initial_dist = manhattan_dist(vector_1=predicted_vect, vector_2=dataframe[list(dataframe.keys())[0]]) # initilise
        word = list(dataframe.keys())[0]
        for i in dataframe:
            if i != word3: # so that it won't predict 3rd word haha!
                temp_manhattan_dist = manhattan_dist(vector_1=predicted_vect,vector_2=dataframe[i])
                if temp_manhattan_dist < initial_dist:
                    word = i
                    initial_dist = temp_manhattan_dist
        return word
    
    if similarity_type == 2:
        '''
            cosine distance comparison
        '''
        initial_dist = cosine_dist(vector_1=predicted_vect, vector_2=dataframe[list(dataframe.keys())[0]]) # initilise
        word = list(dataframe.keys())[0]
        for i in dataframe:
            if i != word3: # so that it won't predict 3rd word haha!
                temp_cosine_dist = cosine_dist(vector_1=predicted_vect,vector_2=dataframe[i])
                if temp_cosine_dist < initial_dist:
                    word = i
                    initial_dist = temp_cosine_dist
        return word
    
    if similarity_type == 3:
        '''
            average of all distances comparison
        '''
        initial_avg_dist = (euclidean_dist(vector_1=predicted_vect, vector_2=dataframe[list(dataframe.keys())[0]]) + manhattan_dist(vector_1=predicted_vect, vector_2=dataframe[dataframe.columns[0]]) + cosine_dist(vector_1=predicted_vect, vector_2=dataframe[dataframe.columns[0]]))/3 # initilise
        word = list(dataframe.keys())[0]
        for i in dataframe:
            if i != word3: # so that it won't predict 3rd word haha!
                temp_avg_dist = (euclidean_dist(vector_1=predicted_vect, vector_2=dataframe[i]) + manhattan_dist(vector_1=predicted_vect, vector_2=dataframe[i]) + cosine_dist(vector_1=predicted_vect, vector_2=dataframe[i]))/3
                if temp_avg_dist < initial_avg_dist:
                    word = i
                    initial_avg_dist = temp_avg_dist
        return word

def read_write_format(input_dir, output_dir, evaluation_file, similarity_type):
    '''
        Task:
        Approach:
    '''
    total_correct_guesses = 0
    total_guesses = 0
    eval_write_format = []
    input_files = [file for file in os.listdir(input_dir) if file.endswith('.txt')]
    for file in input_files:
        print('Loading: {0}'.format(file))
        temp_correctly_guessed =  0
        temp_write_format = []
        with open('{0}/{1}'.format(input_dir, file), 'r') as f:
            lines = f.read().splitlines()
        temp_total_words = len(lines)
        for line in lines:
            words = line.split()
            fourth_word = compare_and_return_fourth_vector(words[0], words[1], words[2],similarity_type)
            if fourth_word == words[3].lower():
                temp_correctly_guessed += 1
            temp_write_format.append(' '.join(words[:3] + [fourth_word + '\n'])) # could use .capitlize() to follow case consistency!!
        with open('{0}/{1}'.format(output_dir,file), 'w') as write_file:
            write_file.write(''.join(temp_write_format))
        print('Done: {0}'.format(file))
        eval_write_format.append(file + '\n')
        eval_write_format.append('ACCURACY: {0}% ({1}/{2})\n'.format(temp_correctly_guessed/temp_total_words, temp_correctly_guessed, temp_total_words))
        total_correct_guesses += temp_correctly_guessed
        total_guesses += temp_total_words
    eval_write_format.append('Total accuracy: {0}% ({1}/{2})'.format(total_correct_guesses/total_guesses, total_correct_guesses, total_guesses))
    with open(evaluation_file, 'w') as eval_file:
        eval_file.write(''.join(eval_write_format))
    return 'Hurray Done!'

# finally: execute everything at once:
read_write_format(input_directory, output_directory, evaluation_file, similarity_type)

'''
if __name__ == '__main__':
    #print(compare_and_return_fourth_vector('dog', 'puppy', 'cat', similarity_type=0))
    input_dir = '/Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/test_folder'
    output_dir = '/Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/OutputGoogleTestSet'
    print(read_write_format(input_dir, output_dir, 'eval_file', 0))
'''

'''
Commands to learn:
    mkdir output00 output01 output02 output10 output11 output12
    ./word_analogy.sh vectormodel.txt GoogleTestSet output00 output00/eval.txt 0 0
    ./word_analogy.sh vectormodel.txt GoogleTestSet output01 output01/eval.txt 0 1
    ./word_analogy.sh vectormodel.txt GoogleTestSet output02 output02/eval.txt 0 2
    ./word_analogy.sh vectormodel.txt GoogleTestSet output10 output10/eval.txt 1 0
    ./word_analogy.sh vectormodel.txt GoogleTestSet output11 output11/eval.txt 1 1
    ./word_analogy.sh vectormodel.txt GoogleTestSet output12 output12/eval.txt 1 2
'''

'''
    My paths:
    /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet

    ./word_analogy.py vector_model_5_10.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output00 output00/eval.txt 0 0
'''