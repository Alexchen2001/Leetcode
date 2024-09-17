# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        queue = deque([root])
        currLevel = 0
        


        while queue:
            n = len(queue)
            if currLevel % 2 == 1:
                prevNum = float('inf')
            elif currLevel % 2 == 0:
                prevNum = float('-inf')
            
            for _ in range(n):
                node = queue.popleft()
                nodeVal = node.val
                # odd Level ( Even Num decreasing)
                if currLevel % 2 == 1:
                    if prevNum > nodeVal and nodeVal % 2 == 0:
                        prevNum = nodeVal
                    else:
                        return False
                # Even Level (Odd Num Increasing)
                elif currLevel % 2 == 0:
                    if prevNum < nodeVal and nodeVal % 2 == 1:
                        prevNum = nodeVal
                    else:
                        return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            currLevel += 1
        return True
            


        