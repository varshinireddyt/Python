# Binary Search
pos = -1
def search(list,target):
    start = 0
    end = len(list)-1
    while start <= end:
        mid = (start + end) // 2

        if list[mid] == target:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < target:
                start = mid+1
            else:
                end = mid-1
    return False
list = [1,3,5,6,8,9,22,33,55,77,88]
target = 10

if search(list,target):
    print("Found at ", pos+1)
else:
    print("Not Found")