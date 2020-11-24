#Problem A -- Weighted random choice
def weighted_select(words):
    '''
    Purpose: Take in a dictionary of words and chooses a word randomly based on the proportion of its frequency
    Input Parameter(s): Dictionary of words
    Return Value: word from dictionary, and its frequency of being chosen is based on its respective value in the dictionary
    '''
    import random
    lst = []
    for key in words.keys():
        for i in range(words[key]):
            lst.append(key)
    choice = random.choice(lst)
    return choice

#Problem B -- Bigram count
def bigram_count(string):
    '''
    Purpose: Count all of the bigrams in a given string
    Input Parameter(s): String
    Return Value: Return dictionary of dictionaries that contains bigrams and the counts of their occurrence
    '''
    lst = string.split()
    out_dict = {}
    for i in range(len(lst)-1):
        first = lst[i]
        second = lst[i+1]
        if first in out_dict.keys():
            if second in out_dict[first].keys():
                out_dict[first][second] += 1
            else:
                out_dict[first][second] = 1
        else:
            out_dict[first] = {}
            out_dict[first][second] = 1
    return out_dict

#Problem C -- Random Sentence Generation
def random_sentence(bigram_dict, start_str, length):
    '''
    Purpose:
    Input Parameter(s):
    Return Value:
    '''
    lst = [start_str]
    choice = ''
    for i in range(length - 1):
        if i == 0:
            counts = bigram_dict[start_str]
            choice = weighted_select(counts)
        else:
            if choice in bigram_dict.keys():
                counts = bigram_dict[choice]
                choice = weighted_select(counts)
            else:
                choice = start_str

        lst.append(choice)
    out = ' '.join(lst)
    return out

#Problem D -- Loading data from files
def rand_sent_file(fname, length):
    '''
    Purpose:
    Input Parameter(s):
    Return Value:
    '''
    import random
    fp = open(fname, 'r')
    string = fp.read()
    stringlist = string.split()
    randint = random.randint(0, len(stringlist))
    start = stringlist[randint]
    counts = bigram_count(string)
    out = random_sentence(counts, start, length)
    return out
