
#Problem A
def list_swap(vals, idx1, idx2):
    #use a helper variable to store a value, or use this format
    vals[idx1],vals[idx2] = vals[idx2],vals[idx1]
    return vals
#Example 1
#print(list_swap([-12, 'carrot', '$12.57', 4.5, 9], 1, 3))
#Example 2
#print(list_swap(['A', 'B', 'C', 'D', 'E', 'F'], 2, 5))

#Problem B
#function
def flight_time(height, vert_speed):
    #import
    import math
    #write formula from instructions
    flytime = (vert_speed + math.sqrt((vert_speed)**2 + (19.6 * height))) / 9.8
    return flytime

#Example 1
#print(flight_time(0.0, 9.8))
#Example 2
#print(flight_time(100.0, 0.0))
#Example 3
#print(flight_time(60.0, 20.0))

#Problem C
def secret(word):
    #get the length of the inputted word
    wrdlen = len(word)
    #divide by 2, rounded down. Since indexing starts at 0, this will place the index at the middle of the odd word
    indx = wrdlen // 2
    #by indexing the word, it is now a list instead of a string. Concatenate each desired character in the list into a string.
    ThreeCStr = word[0] + word[indx] + word[-1]
    return ThreeCStr

#Example 1
#print(secret('Rotated'))
#Example 2
#print(secret('Barbarian'))
