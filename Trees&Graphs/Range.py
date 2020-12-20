class Tree:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root,new_node):
    if root is None:
        return Tree(new_node)
    elif root.val >= new_node:
        root.left = insert(root.left,new_node)
    else:
        root.right = insert(root.right,new_node)

    return root

def rangeElements(root,start,end,res):
    if root is None:
        return res
    if root.val < start:
        #res.append(root.val)
        rangeElements(root.right,start,end,res)
    elif root.val > end:
        rangeElements(root.left,start,end,res)
    elif start <= root.val <= end:
        res.append(root.val)
        rangeElements(root.left,start,end,res)
        rangeElements(root.right,start,end,res)

    return res

root = Tree(8)
#arr = [2,35,1,42,5.2,9,10]
arr = [6,5,7,15,12,17]
for i in range(len(arr)):
    insert(root,arr[i])

#inOrder(root)

start = 7
end = 15
res = []
print(rangeElements(root,start,end,res))




