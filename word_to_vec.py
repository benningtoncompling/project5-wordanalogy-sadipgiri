import numpy as np

def word_to_vec_dict(model_file):
    '''
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
            Formulae: vec/mag(vec)
                where, mag(vec) is the square root of sum of squares of the vector
            Could use numpy for faster arithmic!
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
    print(word_to_vec_dict('smaller_model.txt'))