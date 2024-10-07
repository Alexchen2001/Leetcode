# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        def dfs(node, remain, skipped):
            nonlocal count
            if not node:
                return 
            if skipped:
                dfs(node.left, remain, True)
                dfs(node.right,remain, True)
            
            if remain == node.val:
                count += 1

            dfs(node.left, remain - node.val, False)
            dfs(node.right, remain - node.val , False)

        dfs(root, targetSum, True)
        return count 

        