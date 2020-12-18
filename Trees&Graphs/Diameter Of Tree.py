class Tree:
    def __init__(self,root,left=None,right=None):
        self.root = root
        self.left = left
        self.right = right

def diameter(root,diam):
    if root is None:
        return 0,diam
    leftHeight, diam = diameter(root.left,diam)
    rightHeight, diam = diameter(root.right,diam)

    maxDiameter = leftHeight + rightHeight + 1
    diam = max(diam, maxDiameter)
    return max(leftHeight,rightHeight) + 1, diam

def BinaryDiameter(root):
    diam = 0
    return diameter(root,diam)[1]


if __name__ == '__main__':
    root = Tree(1)
    root.left = Tree(2)
    root.right = Tree(3)
    root.left.right = Tree(4)
    root.right.left = Tree(5)
    root.right.right = Tree(6)
    #diam = 0

    print('Diameter : ', BinaryDiameter(root))