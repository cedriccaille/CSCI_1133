#Problem A -- DNA Complement
def complement(DNA):
    '''
    Purpose: Take in a DNA sequence and produce a complementary strand
    Input Parameter(s): DNA - type: string. short single strand DNA sequence
    Return Value: Complementary strand to the DNA. Type: string
    '''
    strand = DNA.lower()
    out = []
    nucs = ['a','t','g','c']
    for ch in strand:
        if ch == 'a':
            ch = 't'
        elif ch == 't':
            ch = 'a'
        elif ch == 'g':
            ch = 'c'
        elif ch == 'c':
            ch = 'g'
        elif ch not in nucs:
            ch = ''
        out.append(ch)
    comp = ''.join(out)
    return comp
    
#Problem B -- DNA Codon Marking
def mark(strand):
    '''
    Purpose: Take in DNA strand and produces strand between the start and stop codons
    Input Parameter(s): strand - type: string. Short single strand DNA sequence
    Return Value: new sequence between the start (>>>) and stop (<<<) codons.
    '''
    start = ['atg']
    stop = ['taa', 'tag', 'tga']
    startarrow = '>>>'
    stoparrow = '<<<'
    out = []
    i = 0
    while i < len(strand):
        codon = strand[i:i+3]
        if codon in start:
            out.append(startarrow)
        elif codon in stop:
            out.append(stoparrow)
        else:
            out.append(codon)
        i += 3
    newstrand = ''.join(out)
    return newstrand

#Problem C -- Spam Email Dictionary
def spam_table(spam, not_spam):
    '''
    Purpose: Take in two lists of strings and returns a dictionary that counts the similar words between them
    Input Parameter(s): Two lists of strings. One is a spam email, the other is not a spam email
    Return Value: Dictionary, where all keys are words in either email, and the value is the freqeuncy that it appears in spam emails
    '''
    spamstring = ' '.join(spam)
    notspamstring = ' '.join(not_spam)
    convert_spam = spamstring.lower()
    convert_notspam = notspamstring.lower()
    spamdict = {}
    exspamlist = convert_spam.split(' ')
    exnotspamlist = convert_notspam.split(' ')
    for word in exspamlist:
        spamdict[word] = exspamlist.count(word)
        spamdict[word] -= exnotspamlist.count(word)
    for word1 in exnotspamlist:
        spamdict[word1] = exspamlist.count(word1)
        spamdict[word1] -= exnotspamlist.count(word1)
    return spamdict

#Problem D -- Spam Email Prediction
def spam_check(email, table):
    '''
    Purpose: take in an email and the dictionary from spam_table(), then return total spam score of email
    Input Parameter(s): email -- email to check. table -- result from spam_table(), dictionary type.
    Return Value: Total spam score of email, integer.
    '''
    total_score = 0
    convert_email = email.lower()
    emaillist = convert_email.split(' ')
    for i in range(len(emaillist)):
        if emaillist[i] in table:
            total_score += table[emaillist[i]]
    if total_score > 0:
        print("Spam")
    elif total_score <= 0:
        print("Not Spam")
    return total_score
