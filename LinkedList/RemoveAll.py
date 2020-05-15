"""
Leetcode: Remove Linked List Elements: Remove all elements from a linked list of integers that have value val.
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = None
    def removeElements(self, head, val):
        prev = ListNode(-1)
        prev.next = head
        current = prev
        while current.next is not None:
                if  current.next.val == val:
                    current.next = current.next.next
                else:
                    current = current.next
        return prev.next