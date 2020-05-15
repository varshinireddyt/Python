"""
LeetCode: Write a function to delete a node (except the tail) in a singly linked list,
given only access to that node.
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5,
the linked list should become 4 -> 1 -> 9 after calling your function.
"""
class ListNode(object):
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def __init__(self):
        self.head = None
    def insert(self,data):
        node = ListNode(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current  = current.next
##Solution
    def deleteNode(self,node):
        node.data = node.next.data
        node.next = node.next.next





l = Solution()
l.insert(4)
l.insert(5)
l.insert(1)
l.insert(9)
# l.printList()
l.deleteNode(5)
l.printList()