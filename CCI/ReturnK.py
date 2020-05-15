"""
Solution 2.2:Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
Input: 10->0->99, K = 3
Output: 10
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
    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
#By two pointers
    def returnToLast(self, K):
        current = second = self.head
        for i in range(K):
            if second is None:
                return None
            second = second.next
        while second:
            current = current.next
            second = second.next
        return current
# By Calculating the total size
    def returnKth(self,K):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        len = count - K + 1
        current = self.head
        for i in range(len):
            current = current.next
        return current.data

















l = LinkedList()
l.insert(10)
l.insert(0)
l.insert(99)
# l.insert(12)
# l.insert(10)
l.printList()
l.returnKth(3)
l.printList()