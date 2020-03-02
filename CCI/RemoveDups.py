"""
Solutions 2.1: Remove Duplicate: Write code to remove duplicates from an unsorted linked list.
Time Complexity: O(n*2)
"""
#Using Two Pointers

class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

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
            current = current.next

    def removeDups(self):
        first = second =self.head
        while first is not None:
           while second.next is not None:
                if second.next.data == first.data:
                    second.next = second.next.next
                else:
                    second = second.next

           first = second = first.next


l = LinkedList()
l.insert("F")
l.insert("O")
l.insert("L")
l.insert("L")
l.insert("O")
l.insert("W")
l.insert("U")
l.insert("P")

# l.printList()
l.removeDups()
l.printList()



