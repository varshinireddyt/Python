"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

def dfs(root):
    output = []
    queue = []
    dummy = Node(0)
    head = Node(0)
    pre = head
    queue.append(root)
    queue.append(dummy)
    while queue:
        current = queue.pop(0)
        if current != dummy:
            pre.next = current
            pre =pre.next
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        else:
            pre.next = None
            output.append(head.next)
            if not queue:
                break
            head.next = queue[0]
            pre = head
            queue.append(dummy)
    return output



def printList(list):
    for node in list:
        while node:
            print(node.val)
            node = node.next

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')

#bst_to_linkedlist(root)
printList(dfs(root))




