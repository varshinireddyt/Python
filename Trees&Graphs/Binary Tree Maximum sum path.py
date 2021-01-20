


"""

There are tfour possible ways to get the maximum sum path
1. Node itself
2. Left Child + Node or Right Child + node
3. Left Child + right Child + node

"""
import math
# result = -math.inf

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxSumPath(root):
    if root is None:
        return 0

    leftChild = maxSumPath(root.left)
    rightChild = maxSumPath(root.right)

    tempSum = max(root.val, max(leftChild,rightChild)+root.val)

    totalSum = max(tempSum, leftChild + rightChild + root.val)

    maxSumPath.result = max(maxSumPath.result, totalSum)
    # global result
    # if totalSum > result:
    #     result =  totalSum
    return tempSum

def findSum(root):
    maxSumPath.result =  -math.inf
    maxSumPath(root)
    return maxSumPath.result




root = Node(10)
root.left = Node(2)
root.right   = Node(10);
root.left.left  = Node(20);
root.left.right = Node(1);
root.right.right = Node(-25);
root.right.right.left   = Node(3);
root.right.right.right  = Node(4);
#maxSumPath(root)
print(findSum(root))

