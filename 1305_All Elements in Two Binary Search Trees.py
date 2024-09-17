# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr1 = []
        arr2 = []

        def dfs(node, arr):
            if not node:
                return 
            
            dfs(node.left, arr)
            arr.append(node.val)
            dfs(node.right, arr)
        dfs(root1, arr1)
        dfs(root2, arr2)
        
        res = []
        res = arr1 + arr2
        res.sort()
        return res




        