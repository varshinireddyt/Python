#add two lists
#LeetCode: Add Two Numbers
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode,)-> ListNode:
        carry = 0
        l3 = ListNode(0)
        current = l3
        while l1 or l2 or carry:
            list1 = 0 if l1 is None else l1.val
            list2 = 0 if l2 is None else l2.val
            val = carry + list1 + list2
            carry = val//10
            current.next = ListNode(val%10)
            current = current.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return l3.next



