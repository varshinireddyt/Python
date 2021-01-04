"""
Segment Tree:
Given an array of integers. we have to do two operations:
1.Update the value at a given index
2.Find maximum between u and v

"""
from math import ceil, log2
class SegmentTree:
    def build(self, tree, arr, node, begin,end):

        if begin == end:
            #print( arr[begin])
            tree[node] = arr[begin]
            # return tree
        else:
            mid = (begin + (end)) // 2
            #print(mid)
            self.build(tree, arr, 2*node, begin, mid)
            self.build(tree, arr, (2*node) +1, mid+1,end)
            tree[node] = max(tree[2*node ],tree[(2*node)+1])
        return tree

    def update(self, tree, arr, node, begin, end, id, newVal):
        if begin == end:
            arr[id] = newVal
            tree[node] = newVal
        else:
            mid = (begin+end) / 2
            if begin <= id and mid >= id:
                self.update(tree, arr, 2*node, begin, mid, id, newVal)
            else:
                self.update(tree, arr, (2 * node)+1, mid+1, end, id, newVal)

            tree[node] = max(tree[2*node],tree[(2*node)+1])

        return tree

    def query(self, tree, node, begin, end, u, v):
        if u > end or v < begin:
            return INT_MIN
        if u <= begin and v >= end:
            return tree[node]
        mid = (begin+end) / 2
        leftChild = self.query(tree, 2*node, begin, mid, u, v )
        rightChild = self.query(tree, (2 * node)+1,  mid+1, end, u, v)
        return max(leftChild,rightChild)

arr = [1,2,5,3,7,6]
n = len(arr)
x = (int)(ceil(log2(n)))
tree= [0] * (2 * (int)(2**x))
treeObj = SegmentTree()
print(treeObj.build(tree, arr, 1, 0, len(arr)-1))


