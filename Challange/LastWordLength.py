
def lengthOfLastWord(self, s):
    words = s.split(' ')
    # print(words)
    word = [w for w in words if w != '']
    if len(word) == 0:
        answer = 0
    else:
        word = word[-1]
        answer = len(word)
    return answer

def lengthLastWord(s):
    ss = 0
    c = 0
    idx = len(s) - 1
    for i in range(len(s) - 1, -1, -1):
        if s[i] == " ":
            idx = idx - 1
        else:
            break
    for i in range(idx, -1, -1):
        if s[i] == " ":
            ss = max(ss, c)
            c = 0
            break
        else:
            c += 1
    return max(ss,c)




s = 'cutie b  '
print(lengthLastWord(s))

#print(len(s))