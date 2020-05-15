class ListNode:
    def __init__(self,x):
        self.data = x
        self.next = None
class Solution:
    def __init__(self):
        self.head = None
    def insert(self,new_data):
        new_data = ListNode(new_data)
        if self.head is None:
            self.head = new_data
        else:
            new_data.next = self.head
            self.head = new_data

    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    def deleteMiddle(self):               #using two pointers
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        middle = count // 2    #calculate the middle length
        prev = ListNode(-1)
        prev.next  = self.head
        current = prev
        for i in range(middle):
            current = current.next
            prev = prev.next
        prev.next = current.next
        current.next = current.next.next
        return current

l = Solution()
l.insert(10)
l.insert(0)
l.insert(99)
l.insert(100)
l.insert(2)


l.deleteMiddle()
l.printList()


