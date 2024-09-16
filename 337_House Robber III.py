# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dp(node, robbed):
            if not node:
                return 0
            
            #skip
            res = dp(node.left,False) + dp(node.right, False)

            #rob only if previously not robbed
            if not robbed:
                res = max(res, node.val + dp(node.left, True) + dp(node.right,True))

            return res
        return dp(root,False)


            


        