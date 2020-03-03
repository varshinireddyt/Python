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

    """
    LeetCode 84: Remove Duplicates from sorted list II
    Input: 1->2->3->3->4->4->5
    Output: 1->2->5
    """
    def removeDuplicate(self, head: ListNode) -> ListNode:
        temp = ListNode(0)
        current = temp
        duplicate = 0
        while head and head.next:
            if head.val != head.next.val:
                if not duplicate:
                    current.next = head
                    current = current.next
                duplicate = 0
            else:
                duplicate = 1
            head = head.next
        current.next = None if duplicate else head
        return temp.next