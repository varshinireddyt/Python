from collections import Counter
def findAnagrams(s,p):
    l1,l2 = len(s),len(p)
    if l1 == 0 or l2 > l1:
        return []
    p_count = Counter(p)
    s_count = Counter()
    res = []
    for i in range(l1):
        s_count[s[i]] += 1

        if i >= l2:
            if s_count[s[i-l2]] == 1:
                del s_count[s[i-l2]]
            else:
                s_count[s[i-l2]] -= 1
        if s_count == p_count:
            res.append(i-l2+1)
    return res

s = "cbaebabacd"
p = "abc"
# s= "aab"
# p= "abaaa"
# print(findAnagrams(s,p))

#using arrays
def findAllAnagrams(s,p):
    l1,l2 = len(s),len(p)
    if l1 == 0 or l2 > l1:
        return []
    p_count = [0] * 26
    s_count = [0] * 26
    res = []
    for i in p:
        p_count[ord(i)-ord('a')] += 1

    for j in range(l1):
        s_count[ord(s[j])-ord('a')] += 1
        if j >= l2:
            s_count[ord(s[j-l2]) - ord('a')] -= 1

        if p_count == s_count:
            res.append(j-l2+1)

    return res

print(findAllAnagrams(s,p))