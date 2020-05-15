"""
Solution 2.3:Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the
first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.

LeetCode: Write a function to delete a node (except the tail) in a singly linked list,
given only access to that node.
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5,
the linked list should become 4 -> 1 -> 9 after calling your function.

"""

from LinkedList import LinkedList
def deleteNode(node):
    node.value = node.next.value
    node.next = node.next.next


l = LinkedList()
l.add_multiple([1,2,3,4,5])
middle_node = l.add(6)
l.add_multiple([7,8,9])

print(l)
deleteNode(middle_node)
print(l)