

#Level Order using BFS or using queue
from queue import Queue
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        result = []
        q = Queue()
        q.put(root)
        while not q.empty():
            currentLevel = []
            length = q.qsize()
            for i in range(length):
                x = q.get()
                if x.left:
                    q.put(x.left)
                if x.right:
                    q.put(x.right)
                currentLevel.append(x.val)
            result.append(currentLevel)
        return result