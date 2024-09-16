# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node, arr):
            if not node:
                return 
            if not node.left and not node.right:
                arr.append(node.val)
            
            dfs(node.left, arr)
            dfs(node.right, arr)

            return arr
        
        arr1 = dfs(root1, [])
        arr2 = dfs(root2,[])

        return arr1 == arr2

