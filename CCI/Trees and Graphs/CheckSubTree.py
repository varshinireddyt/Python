"""
4.10 Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
algorithm to determine if T2 is a subtree of Tl.
A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
"""
class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None

def isIdentical(s1,s2):

    if s1 == None and s2 == None:
        return True

    if s1 != None and s2 != None:
        if s1.data == s2.data and isIdentical(s1.left,s2.left) and isIdentical(s1.right,s2.right):
            return True

    return  False

def checkSubTree(m,s):
    if s is None:
        return True
    if m is None:
        return False
    if isIdentical(m,s):
        return True
    return checkSubTree(m.left,s) or checkSubTree(m.right,s)

main = Node(26)
main.right = Node(3)
main.right.right  = Node(3)
main.left = Node(10)
main.left.left = Node(4)
main.left.left.right = Node(30)
main.left.right = Node(6)

S = Node(10)
S.right = Node(6)
S.left = Node(4)
S.left.right = Node(30)

if checkSubTree(main,S):
    print('Subtree')
else:
    print('not a subtree')