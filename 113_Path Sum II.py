# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, arr, sumNum):
            nonlocal res
            if not node:
                return
            
            arr.append(node.val)
            sumNum += node.val

            if node.left or node.right:
                dfs(node.left, arr, sumNum)
                dfs(node.right, arr, sumNum)
            else:
                dfs(node.left, arr, sumNum)
                if sumNum == targetSum:
                    res.append([num for num in arr])
                
            arr.pop()
            
        if not root:
            res = []
        else:
            dfs(root, [], 0)
        return res

        