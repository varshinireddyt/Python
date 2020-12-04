
def anagrams(arr):
    dict = {}  #key: string, value: list of strings
    for i in range(len(arr)):
        val = "".join(sorted(arr[i]))
        if val in dict.keys():
            value = dict[val]
            value.append(arr[i])
            dict[val] = value
        else:
            dict[val] = [arr[i]]
    return dict.values()

arr = ['act','dog','cat','tac','god']
print(anagrams(arr))








