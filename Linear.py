# Linear Search
pos = -1
def search(list, target):
     i = 0
     while i < len(list):
         if list[i] == target:
             globals()['pos'] = i
             return True
         i = i + 1
     return False

list = [2,12,34,1,10,19]
target = 90

if search(list,target):
    print("Target found at ", pos+1)
else:
    print("Not Found")