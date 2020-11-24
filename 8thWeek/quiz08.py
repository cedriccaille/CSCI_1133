#Problem A -- Slicing
def odds_evens(seq):
    seqlist = seq[:]
    evens = seqlist[0:len(seqlist)+1:2]
    odds = seqlist[1:len(seqlist):2]
    out = odds + evens
    return out

#Problem B -- List of Lists
def count_div5(nested_list):
    count = []
    num = 0
    for i in range(len(nested_list)):
        for j in range(len(nested_list[i])):
            if nested_list[i][j] % 5 == 0:
                num += 1
        count.append(num)
        num = 0
    return count

#Problem C -- All Pairs
def common_start(word_list):
    out = []
    finallst = []
    for i in range(len(word_list)):
        for j in range(i+1, len(word_list)):
            if word_list[i][0] == word_list[j][0]:
                out.append(word_list[i])
                out.append(word_list[j])
    for k in range(len(out)):
        if out[k] not in finallst:
            finallst.append(out[k])
    return finallst
