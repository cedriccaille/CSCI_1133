#Problem A -- Add question marks to each word
def question_everything(phrase):
    '''
    Purpose: Take in phrase and return string that has a question mark after every word
    Input Parameter(s): Phrase - string, series of words separated by spaces
    Return Value: String that has all the original words with a question mark after each
    '''
    nospaces = phrase.split()
    out = '? '.join(nospaces) + '?'
    return out

def alternate_caps(word):
    '''
    Purpose: Takes in a string, alternates the capitalization of each letter, then returns the word
    Input Parameter(s): word -- string
    Return Value: same word as inputted, but every other letter is capitalized
    '''
    lst = ['']
    lower = word.lower()
    for i in range(len(lower)):
        if i % 2 == 0:
            lst.append(lower[i])
        else:
            lst.append(lower[i].upper())
    out = ''.join(lst)
    return out

#Problem C -- Extract URLs
def extract_url(html):
    '''
    Purpose: Take in string of html text with one URL link, then returns only the URL
    Input Parameter(s): html -- string
    Return Value: string, only the URL without the original text
    '''
    idxstart = html.find('href="') + 6
    idxend = html.find('"', idxstart)
    substring = html[idxstart:idxend]
    return substring
