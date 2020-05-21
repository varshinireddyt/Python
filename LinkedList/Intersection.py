"""
Intersection of Two Linked Lists
"""
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def insert(val):
    new_val = ListNode(val)
    new_val.val =  val
    new_val.next = None
    return new_val
def findLength(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count
def getIntersectionNode(l1,l2):
        head1,head2 = l1, l2
        len1,len2 = 0,0
        len1 =findLength(head1)
        len2 =findLength(head2)
        head1,head2 = l1,l2
        if len2 > len1:
            for i in range(len2-len1):
                head2 = head2.next
        elif len1 > len2:
            for i in range(len1-len2):
                head1 = head1.next
        while head2 != head1:
            head1 = head1.next
            head2 = head2.next
        return head1.val






l1 = insert(4)
l1.next = insert(1)
l1.next.next = insert(8)
l1.next.next.next = insert(4)
l1.next.next.next.next = insert(5)

l2 = insert(5)
l2.next = insert(0)
l2.next.next = insert(1)
l2.next.next.next = insert(8)
l2.next.next.next.next = insert(4)
l2.next.next.next.next.next = insert(5)

res = getIntersectionNode(l1,l2)
print(res)