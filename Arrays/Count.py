def countDistinctElement(arr,num):
    res = []
    for i in range(len(arr)-num+1):
        temp = arr[i:i+num]
        dict = {}
        for j in range(len(temp)):
            if temp[j] not in dict.keys():
                dict[temp[j]] =1
            else:
                dict[temp[j]] += 1
        res.append(len(dict))
    return res


arr = [2,1,1,3,1,4,2]
num = 3

print(countDistinctElement(arr,num))

