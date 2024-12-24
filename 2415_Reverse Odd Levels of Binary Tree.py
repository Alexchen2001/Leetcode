from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        currL = [root]
        currVals = []

        while len(currL) > 0:
            nextL =[]
            nextVals = []
            arrLen = len(currL)
            for i in range(arrLen):
                if level % 2 != 0:
                    currL[i].val = currVals[arrLen - i - 1]
                node = currL[i]

                if node.left:
                    nextL.append(node.left)
                    nextVals.append(node.left.val)
                if node.right:
                    nextL.append(node.right)
                    nextVals.append(node.right.val)
            currL = nextL
            currVals = nextVals
            level += 1

        return root
            
            

