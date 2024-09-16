# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfsL(node):
            if not node:
                return None
            ans = []
            ans.append(node.val)
            ans.append(dfsL(node.left))
            ans.append(dfsL(node.right))
            return ans

        
        def dfsR(node):
            if not node:
                return None
            ans = []
            ans.append(node.val)
            ans.append(dfsR(node.right))
            ans.append(dfsR(node.left))
            return ans
        
        arr1 = dfsL(root.left)
        arr2 = dfsR(root.right)

        return arr1 == arr2




            
            