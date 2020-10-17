class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        def postorder(root):
            return postorder(root.left)+postorder(root.right)+[root.val] if root else []
        return ''.join(map(str,postorder(root)))

    def deserialize(self,data):
        def helper(lower=float('-inf'),upper=float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None

            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val,upper)
            root.left = helper(lower,val)
            return root

        #including delimeter('')

        data = [int(x) for x in data.split(' ') if x]
        return helper()

#approach 2 by converting int to string
class Codec:
    def int_to_str(self,x):
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str
    def postorder(self,root):
        return self.postorder(root.left)+self.postorder(root.right)+ [root.val ] if root else []

    def serialize(self,root):
        tree = self.postorder(root)
        tree = [self.int_to_str(x) for x in tree]
        return 'c'.join(map(str,tree))
    def str_to_int(self,bytes_str):
        res = 0
        for ch in bytes_str:
            res = res * 256 + ord(ch)

        return res

    def deserialize(self, data):
        def helper(lower=float('-inf'),upper=float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None

            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val,upper)
            root.left = helper(lower,val)
            return root
        data = [self.str_to_int(x) for x in data.split(' ') if x]
        return helper()



root = TreeNode(4)
# root = insert.insertIntoBST(root,2)
# root = insert.insertIntoBST(root,7)
# root = insert.insertIntoBST(root,1)
# root = insert.insertIntoBST(root,3)
# root = insert.insertIntoBST(root,5)
ser = Codec()
deser = Codec()
tree = ser.serialize(root)
ans = deser.deserialize(tree)
print(ans)



