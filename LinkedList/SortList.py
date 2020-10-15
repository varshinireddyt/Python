class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def insert(self, data):

        new_node = ListNode(data)

        # if head is None, initialize it to new node
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next

        # Append the new node at the end
        # of the linked list
        curr_node.next = new_node

    def getMiddle(self, head):
        if head is None:
            return head
        mid = head
        first = head
        while first.next != None and first.next.next != None:
            mid = mid.next
            first = first.next.next
        return mid


    def mergeSort(self, left, right):

        result = None

        if left is None:
            return right
        if right is None:
            return left

        if left.val <= right.val:
            result = left
            result.next = self.mergeSort(left.next, right)
        else:
            result = right
            result.next = self.mergeSort(left, right.next)
        return result

    def sortList(self, head):
        if head is None or head.next is None:
            return head
        middle = self.getMiddle(head)
        next_middle = middle.next

        middle.next = None

        left = self.sortList(head)

        right = self.sortList(next_middle)

        sortedlist = self.mergeSort(left,right)
        return sortedlist

def printList(head):
    if head is None:
        print(' ')
        return
    current = head
    while current.next:
        print(current.val)
        current = current.next
    print( ' ')


if __name__ == '__main__':

    li = Solution()
    li.insert(4)
    li.insert(2)
    li.insert(1)
    li.insert(3)

    li.head = li.sortList(li.head)
    printList(li.head)





