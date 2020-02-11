class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class RotateList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head

    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next

    def rotateRight(self, head, k: int) -> ListNode:
        if not head:
            return None
        temp = head
        count = 0
        # Finding the length of the list
        while temp is not None:
            temp = temp.next
            count +=1

        rotateRight = k%count
        if k == 0 or rotateRight == 0:
            return head
        for _ in range(rotateRight):
            temp = temp.next

        first = second = head
        while first is not None:
            first = first.next
            second = second.next

        temp = second.next
        second.next = None
        first.next = head
        head = temp

        return head

llist = RotateList()
for i in range(5, 0, -1):
    llist.push(i)
print("Given List: ")
llist.printList()
llist.rotateRight(2)

print("Rotate Linked List: ")
llist.printList()

