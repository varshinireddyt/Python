"""
LeetCode 83: Remove Duplicates from sorted list
TimeComplexity: O(n)
"""
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

