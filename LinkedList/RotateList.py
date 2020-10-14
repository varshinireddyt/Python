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
        if not head.next:
            return head
        temp = head
        count = 1
        # Finding the length of the list
        while temp.next:
            temp = temp.next
            count +=1
        rotate_right = k % count
        # if k== 0 then no rotation is required
        if k == 0 or rotate_right == 0:
            return head
        temp.next = head
        new_tail = head
        for _ in range(count - k % count - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head



llist = RotateList()
rotate = RotateList()
for i in range(5, 0, -1):
    llist.push(i)
print("Given List: ")
llist.printList()
llist.rotateRight(llist,2)

print("Rotate Linked List: ")
rotate.printList()

