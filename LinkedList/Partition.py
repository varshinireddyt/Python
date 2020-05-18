"""
LeetCode: Partition List:Given a linked list and a value x, partition it such that all nodes less than x come before
nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""
class ListNode:
    def __init__(self):
        self.data = 0
        self.next = None

def insert(data):
    new_data = ListNode()
    new_data.data = data
    new_data.next = None
    return new_data

def printList(head):
    current = head
    while current:
        print(current.data)
        current = current.next
#using two pointers
def partition(head,x):
    first_head = first_tail = ListNode()
    second_head = second_tail = ListNode()
    while head is not None:
        if head.data < x:
            first_head.next = head
            first_head = first_head.next
        else:
            second_head.next = head
            second_head = second_head.next
        head = head.next
    second_head.next = None
    first_head.next  = second_tail.next
    return first_tail.next

head = insert(1)
head.next = insert(4)
head.next.next = insert(3)
head.next.next.next = insert(2)
head.next.next.next.next = insert(5)
head.next.next.next.next.next = insert(2)

head = partition(head,3)
printList(head)

