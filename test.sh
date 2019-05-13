#!/bin/bash

# Bash script to execute all commands at once as specified
# Author: Sadip Giri (sadipgiri@bennington.edu)
# Date: 11th May 2019

# At first, make all required directory
mkdir output00 output01 output02 output03 output10 output11 output12 output13
# NOTE: here-> 1st 0 means should_normalize or not (1) and 
# 2nd 0 means Euclidean distance, 1 manhattan distance, 2 cosine distance & 3 average of all those distances (I created to see the underlying difference)

./word_analogy.py vector_model_5_10.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output00 output00/eval.txt 0 0
./word_analogy.py vector_model_5_10.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output01 output01/eval.txt 0 1
./word_analogy.py vector_model_5_10.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output02 output02/eval.txt 0 2
./word_analogy.py vector_model_5_10.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output03 output03/eval.txt 0 3
./word_analogy.py vector_model_5_10.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output10 output10/eval.txt 1 0
./word_analogy.py vector_model_5_10.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output11 output11/eval.txt 1 1
./word_analogy.py vector_model_5_10.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output12 output12/eval.txt 1 2
./word_analogy.py vector_model_5_10.txt /Users/sadipgiri/Desktop/project5-wordanalogy-sadipgiri/GoogleTestSet output13 output13/eval.txt 1 3
