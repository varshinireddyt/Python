#Leetcode: Merge K Sorted Lists
"""
Time Complexity: O(NlogK), N is the size of the Merged List, K is the size of the lists
Space Complexity: O(1)
Using Divide and Conquer method

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class KSorted:

    def mergeKLists(self, lists):
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)//2
        begin = lists[:mid]
        end = lists[mid:]
        return self.mergeTwoLists(begin,end)

    def mergeTwoLists(self, l1, l2):
        temp = dummy = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2
        return dummy.next


