from collections import defaultdict


def isUnique(input):
    unique = [i for i in range(65, 91)] + [i for i in range(97, 123)]
    char = defaultdict(int)
    for i in unique:
        char[i] = False
    for i in input:
        asci = ord(i)
        if asci in char:
            if char[asci] == False:
                char[asci] = True
            else:
                return 'No'

    return 'Yes'



def unique(input):
    char = defaultdict(int)
    for i in range(65,91):
        char[i] = False
    for j in range(97,123):
        char[j] = False
    for i in input:
        asci = ord(i)
        if asci in char:
            if char[asci] == False:
                char[asci] = True
            else:
                return 'No'

    return 'Yes'


input = 'I am wonderful'
#print(isUnique(input))
print(unique(input))