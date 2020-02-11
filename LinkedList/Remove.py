# Leetcode: Remove the Nth node from the end of the list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self):
        self.head = None

    def removeNthFromEnd(self, head: ListNode, n: int)-> ListNode:
        # Two Pass Algorithim
        """If length < position then we can't remove the node
            If length = position then return head->next
            If lenggth > position then delete its intermediate node and pointits previous node to its next node"""
        temp = head
        count = 0
        #Finding the length from the begining
        while temp is not None:
            temp = temp.next
            count += 1
        len = count - n
        #Two pointers from the begining
        prev = None
        current = head
        while len != 0:
            prev = current
            current = current.next
            len -= 1
        if prev is None:
            return head.next
        else:
            prev.next = current.next
            current.next = None
            return head







