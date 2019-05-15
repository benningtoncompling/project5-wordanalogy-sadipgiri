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
        Euclidean(80.69484240687679%), Cosine(80.69484240687679%) and Avg(80.04502660663118%) Similarities gave slightly higher accuracy than Manhattan (79.83012689316415%)

    However, using vectormodel.txt (as you can see in output folders): there was very low accuracy since many words were missing! As a result, I didn't find it interesting enough to compare similarities as well as investigate effect of normalization.

    Having said that, larger model (samplemodel.txt) gave approx 50% accuracy whereas it took very long time to even compute evaluation file for Euclidean Similarity without normalization. [Check: samplemodel_outputs folder for further details]

Since, vector_model_5_10.txt was already normalized; so, I didn't get to see accuracy differences there. However, I am still running larger word2vec model (e.g. samplemodel.txt) to further investigate normalization effect! I think its all about ACCURACY vs TIME COMPLEXITY tradeoffs and I consider there won't be big of a difference in accuracy. 

Approaches, Optimizations, Roadblocks:
- At first, I used Pandas dataframe to read word2vec model; however, there was time complexity issues while comparing predicted word with all existing words. Therefore, I used dictionary with keys: words and values: vectors (represented by numpy array). Why numpy -> it does calcuation in C-level which is obviously faster than normal Python arithmetic.

- Time complexity optimization:
    - Euclidean Similarity: instead of square_root I just used squares of vectors difference to compare and get most close vector_word -> Faster than square root.
        - Also, instead of squaring: I explored vector transpose operator for faster calculation:
                -> euclidean_distance(x, y) = (x − y)T (x − y) where, T is transpose

    - Cosine Distance: while normalization was not unabled, I just used numpy dot product for cosine distance -> faster than dividing by vector's magnitude
        - NOTE: used 1 - cosine_similarity while averaging all distances (my 3rd similarity type) to get higher acccuracy.

    - Loading vector model: instead of normalizing same vectors over and over; I dynamically read vector model and created a normalized dictionary for faster look up and calculation. I think in long run, this is very helpful and extremely faster (especially, when we have large Word Analogy test files)

- Accuracy Optimization:
    - Ignored fourth predicted word to not to be third word which gave higher accuracy.
    - Similarly, ignoring fourth word be first three words -> further increased the accuracy.
    - Want to:
        - see if there might be some changes in accuracy using other similarities techniques such as:
            - Jaccard Similarity
            - Dice Similarity
            - KL divergence Similarity, etc. 

- Details/Roadblocks:
    - Used bash script to automatically run everything at once rather than having to execute same commands one by one.
    - At first, cosine similarity wasn't working nicely. However, found out that it was because I had to search for the words with higher cosine similarity (credit: Justin). Or could have subtracted by 1 and I would be fine with my initial approach!
    - I really enjoyed learning/exploring various ways to optimize as well as write meaningful clean code (especially, keeping track of everything!).