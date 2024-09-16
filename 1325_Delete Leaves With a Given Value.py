# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val == target and not node.left and not node.right:
                return None
            else:
                return node
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root
        
