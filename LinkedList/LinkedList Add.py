"""
Design an linked list
    Node
    LinkedList Calss
        Append method
        Get Method

Populate the linked list with 357 - 7 --> 5-->3

Populate the linked list with 1378 8-->7-->3-->1

Sum these 2 linked lists

1378 + 357 = 1735



"""


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def appendList(val):
    new_val = Node(val)
    new_val.val = val
    new_val.next = None
    return new_val


def get(current, num):
    while current != None:
        if current.val == num:
            print(num, ' exists in the list')
        current = current.next


def add(l1, l2):
    total = l1.val + l2.val
    carry = int(total / 10)

    l3 = Node(total % 10)
    first = l1.next
    second = l2.next
    third = l3
    while first != None or second != None:
        total = carry + (first.val if first else 0) + (second.val if second else 0)
        carry = int(total / 10)
        third.next = Node(total % 10)
        third = third.next
        first = first.next if first else None
        second = second.next if second else None

    if carry > 0:
        third.next = Node(carry)

    return l3


def printList(l):
    result = []
    while l:
        result.append(l.val)
        l = l.next

    num = ''.join(map(str, result))

    print(num[::-1])


l1 = appendList(7)
l1.next = appendList(5)
l1.next.next = appendList(3)

get(l1, 3)

l2 = appendList(8)
l2.next = appendList(7)
l2.next.next = appendList(3)
l2.next.next.next = appendList(1)

l3 = add(l1, l2)
printList(l3)



