# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        queue = deque([root])
        levelCounter = 0
        Sum = 0
        currMaxLevel = float('-inf')
        currMaxNum = float('-inf')

        while queue:

            currLevelSize = len(queue)
            Sum = 0 
            levelCounter += 1
            for _ in range(currLevelSize):
                node = queue.popleft()
                Sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if Sum > currMaxNum:
                currMaxNum = Sum
                currMaxLevel = levelCounter
        return currMaxLevel







        
        