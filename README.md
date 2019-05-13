# Word2Vec & Word Analogy Project
Program that solves analogies such as "dog is to cat as puppy is to ___".
<br/>
  
## Code Requirements

The code is in Python3 (version 3.0 or higher will work). The only other requirement is: <a href="https://www.numpy.org/">numpy</a>.


### Execution

To run the program, simply run the test.sh file

./test.sh

### Author

* **<a href="https://sadipgiri.github.io">Sadip Giri</a>** - (sadipgiri@bennington.edu)

### Contact

Feel free to contact me or open a ticket (PRs are always welcome!) with any questions, comments, suggestions, bug reports, etc.

### License

This project is licensed under the terms of the MIT license.

### Findings

Among three similarities type:
    0. Euclidean Distance (L1 Norm)
    1. Manhattan Distance (L2 Norm)
    2. Cosine Distance (Dot Product after Normalization)
    3. Avg of all similarities
    Using vector_model_5_10.txt:
        Euclidean(80.69484240687679%) and Cosine(80.69484240687679%) Similarities gave slightly higher accuracy than other similarities such as Manhattan (79.83012689316415%) & Avg() 
    Its because -> 

Since, vector_model_5_10.txt was already normalized; so, I didn't get to see accuracy differences there. However, I am still running larger word2vec model to further investigate normalization effect!

Some ideas to consider:
Which similarity metric seemed to work better? Why do you think that is?
What input files did better than others?
Did normalization help? In what cases?
If you used a different vector model (more below) what did you notice about your
results?