"""
LeetCode: Swap node Pairs
Time Complexity: O(n)
"""
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class SwapPairs:
    def  swapNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        temp = ListNode(0)
        temp.next = head
        dummy = temp
        while dummy.next and dummy.next.next:
            first = dummy.next
            second = dummy.next.next
            dummy.next = second
            first.next = second.next
            second.next = first
            dummy = dummy.next.next
        return temp.next


