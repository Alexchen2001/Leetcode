# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, wentLeft, length):
            nonlocal res

            if not node:
                return 
            if length > res:
                res = length
            
           
            if wentLeft:
                dfs(node.right,False,length + 1)
                dfs(node.left, True, 1)
            else:
                dfs(node.left, True, length + 1)
                dfs(node.right,False, 1)
            
        dfs(root.left, True, 1)
        dfs(root.right, False, 1)
        return res
