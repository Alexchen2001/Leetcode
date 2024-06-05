# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False 
        currSum = targetSum - root.val
        ## the condition checks whether if it is a leaf node
        ## leafNode: a node that does not have any children nodes
        if not root.left and not root.right:
            return currSum == 0
        print("currNode:" + str(root.val))
        print("remaining:" + str(currSum))
        
        leftPath = self.hasPathSum(root.left, currSum)
        rightPath = self.hasPathSum(root.right,currSum)

        return leftPath or rightPath 