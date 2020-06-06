"""
Insert into sorted circular linked list
"""
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,new_val):
        new_node = ListNode(new_val)
        new_node.next = self.head
        self.head =new_node

    def printList(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

    def sortedInsertion(self, new_node):
        current =self.head
        if current is None:
            new_node.next = new_node
            self.head = new_node

        elif current.val >= new_node.val:
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            while current.next != self.head and current.next.val <  new_node.val:
                current = current.next
            new_node.next = current.next
            current.next = new_node



