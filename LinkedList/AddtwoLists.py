"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,node):
        node = ListNode(node)
        if self.head is None:
            self.head = node
        else:
            node.next =  self.head
            self.head = node
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return prev
    def findLength(self, l):
        count = 0
        while l:
            count += 1
            l = l.next
        return count
    def addTwoNumber(self, l1, l2):
        len1, len2 = self.findLength(l1), self.findLength(l2)
        l1 = self.addZeros(len2 - len1, l1)
        l2 = self.addZeros(len1 - len2, l2)
        carry, res = self.addList(l1, l2)
        if carry > 0:
            l3 = ListNode(carry)
            l3.next = res
            res = l3
        return res

    def addZeros(self, diff, node):
        for i in range(diff):
            new = ListNode(0)
            new.next = node
            node = new
        return node

    def addList(self, l1, l2):
        if (not l1 and not l2):
         return (0, None)
        carry, new = self.addList(l1.next, l2.next)
        add = l1.data + l2.data + carry
        res = ListNode(add % 10)
        res.next = new
        return (add // 10, res)

    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
l1 = LinkedList()
l2 = LinkedList()

l1.insert(7)
l1.insert(2)
l1.insert(4)
l1.insert(3)
# l1.printList()
l2.insert(5)
l2.insert(6)
l2.insert(4)
# l2.printList()
add = LinkedList()
add.addTwoNumber(l1.head,l2.head)
add.printList()





