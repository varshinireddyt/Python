"""
Leetcode: Given a singly linked list, determine if it is a palindrome.
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

def isPalindrome(head):
    rev = []
    while head:
        rev.append(head.data)
        head = head.next
    return rev == rev[::-1]

head = insert(1)
head.next = insert(4)
head.next.next = insert(3)
head.next.next.next = insert(2)
head = isPalindrome(head)
print(head)
