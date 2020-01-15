# BubbleSort
def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] < list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

list = [2,5,6,1,12,3,10]
sort(list)
print(list)