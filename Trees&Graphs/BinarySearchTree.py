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


def inOrder(root):
    if root is None:
        return None

    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

root = Tree(8)
arr = [2,35,1,42,5.2,9,10]
for i in range(len(arr)):
    insert(root,arr[i])

inOrder(root)

