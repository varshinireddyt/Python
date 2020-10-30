"""
Given a string and a list of number, split the string according to the list and swap it. Return the swapped string.
For example: given "descognail" and [3,2,3,1,1]
We split the string as "des" = 3, "co" = 2, "gna" = 3, "i" = 1, "l" = 1 like the list
Then we swap "des" with "co", "gna" with "i" and left with "l" (no swap). We then have "codesignal" isntead of the original "descognail".
Then return "codesignal".
"""

def concatenateSwaps(string,size):
    if len(string) == 0 or len(size) == 0:
        return ""
    dict = {}
    a = 0
    b =size[0]
    for i in range(len(size)-1):
        dict[i] = string[a:b]
        a += size[i]
        b+= size[i+1]
    dict[len(size)-1] = string[-size[-1]:]
    value_dict = list(dict.values())
    for i in range(0,len(size)-1,2):
        value_dict[i],value_dict[i+1] = value_dict[i+1],value_dict[i]
    return "".join(value_dict)

string = "descognail"
size = [3, 2, 3, 1, 1]
print(concatenateSwaps(string,size))