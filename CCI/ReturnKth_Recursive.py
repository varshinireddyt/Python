class ListNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None
def insert(data):
    new_node = ListNode(0)
    new_node.data = data
    new_node.next = None
    return new_node
def returnKth(head, K):
    if head is None:
        return
    index = returnKth(head.next,K) + 1
    if index == K:
        print("Kth",head.data)
    return index

# head = ListNode(0)
head = insert(10)
head.next = insert(0)
head.next.next = insert(99)
# l = ListNode(0)
returnKth(head,3)

