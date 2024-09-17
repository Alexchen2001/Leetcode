# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        queue = deque([root])
        res = []

        while queue:
            n = len(queue)
            currSum = 0
            for _ in range(n):
                node = queue.popleft()
                currSum += node.val

                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(currSum / n)
        return res
        
        