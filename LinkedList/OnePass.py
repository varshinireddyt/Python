# Leetcode: Remove the Nth node from the end of the list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self):
        self.head = None

    def removeNthFromEnd(self, head: ListNode, n: int)-> ListNode:
        # Using One Pass Algorithm (Here it uses dummy variable)
        temp = ListNode(0)
        temp.next = head
        first = second = head
        for _ in range(n):
            first = first.next
        while first != None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return temp.next





