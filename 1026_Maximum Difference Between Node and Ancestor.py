# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
            maxDiff = 0
            def dfs(root, minNum = None, maxNum = None):
                nonlocal maxDiff
                if not root:
                    if (maxNum - minNum > maxDiff):
                        maxDiff = maxNum - minNum
                    return 0
                if (minNum== None and maxNum == None):
                    minNum, maxNum = root.val,root.val
                
                if (maxNum < root.val):
                    maxNum = root.val
                if (minNum > root.val):
                    minNum = root.val

                dfs(root.left, minNum, maxNum)
                dfs(root.right, minNum, maxNum)
            
            dfs(root)
            return maxDiff

                

                
        