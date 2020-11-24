def FirLasSame(string1, string2):
    return (string1[0] == string2[0]) and (string1[-1] == string2[-1])

def PullPunct(string):
    out = ' '
    for ch in string:
        if ch in '.?!':
            out += ch
    return out

def Reverse(string):
    out = ''
    for i in range(len(string) - 1, -1, -1):
        out += string[i]
    return out

def Reverse1(string):
    out = ''
    for ch in string:
        out = ch + out
    return out

def Reverse2(string):
    return string[::-1]

nums = [6,3,8,9,12]
word = 'python'

# print(nums[:], word[:])
# print(nums[1:], word[1:])
# print(nums[:-1], word[:-1])
# print(nums[::-1], word[::-1])
# print(nums[:len(nums)//2], word[:len(nums)//2])
# print(nums[len(nums)//2:], word[len(nums)//2:])
# print(nums[2:4], word[2:4])
# print(nums[4:2], word[4:2])
# print(nums[2:4:-1], word[-2:-4:-1])
# print(nums[1:6:2], word[1:6:2])

x = "ChcdosaControl"
y = x.replace('a','e').replace('cd','a').split('a')
print(y)

def Caesar(string):
    out = ''
    for ch in string:
        asc = ord(ch) - ord('A')
        asc += 3
        out += chr(asc%26 + ord('A'))
    return out

def encrypt(string, key):
    out = ''
    for ch in string:
        asc = ord(ch) - ord('a')
        out += key[asc]
    return out

def decrypt(string, key):
    out = ''
    for ch in string:
        idx = key.find(ch)
        asc = idx + ord('a')
        out += chr(asc)
    return out
