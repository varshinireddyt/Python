from queue import LifoQueue

def balanced(arr):
    stack = LifoQueue()

    for  i in range(len(arr)):
        if arr[i] == ']' or arr[i] == '}'  or arr[i] == ')' :
            if stack.empty():
                return False
            c = stack.get()
            if  (c == '[' and arr[i] != ']' ) or (c == '(' and arr[i] != ')' ) or (c == '{' and arr[i] != '}' ):
                return False
        else:
            stack.put(arr[i])
    if stack.empty():
        return True
    return False

arr = '{{{[[(]}}}'
print(balanced(arr))










            
 



