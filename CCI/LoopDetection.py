"""
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier
node, so as to make a loop in the linked list.
Input: A -> B -> C -> D -> E -> C
Output: C
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
        self.head = new_node

    def printList(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next
    def loopDetection(self):
        first = second = self.head
        while first and second and second.next:
            first = first.next
            second = second.next.next
            if first == second:
                print("Loop Detected: ", first.val)
                return
l = LinkedList()
l.insert('A')
l.insert('B')
l.insert('C')
l.insert('D')
l.insert('E')
l.insert('C')
l.head.next.next.next.next.next = l.head
l.loopDetection()
