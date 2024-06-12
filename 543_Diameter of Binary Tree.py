# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(root):
            if not root:
                return 0
            
            nonlocal diameter
            leftTraverse = dfs(root.left)
            rightTraverse = dfs(root.right)

            diameter = max(diameter,leftTraverse + rightTraverse)
            return max(leftTraverse, rightTraverse) + 1

        dfs(root)
        return diameter
            
                