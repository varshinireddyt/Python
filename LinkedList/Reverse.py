"""
Reverse Linked List- O(n)
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

## Using Iterative Approach
def reverseList(head):
    current = head
    prev = None
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev
## Using Recursion Approach
def reverse(head):
    if head is None or head.next is None: return head
    prev = reverse(head.next)
    head.next.next = head
    head.next = None
    return prev

head = insert(1)
head.next = insert(4)
head.next.next = insert(3)
head.next.next.next = insert(2)
# printList(head)

head = reverse(head)
printList(head)
