from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([[root]])
        leftInd = False
        res = []
        if root != None:  
            res.append([root.val])
        while queue:
            nodes = queue.popleft()
            nextLevel = []
            nextLevelVals = []
            
            for node in nodes:
                
                if node != None:
                    if node.left:
                        nextLevel.append(node.left)
                        nextLevelVals.append(node.left.val)
                    if node.right:
                        nextLevel.append(node.right)
                        nextLevelVals.append(node.right.val)
            
            if nextLevel == []:
                break
            else:
                print(nextLevelVals)
                queue.append(nextLevel)
                if leftInd:
                    res.append(nextLevelVals)
                else:
                    res.append(nextLevelVals[::-1])
                leftInd = not leftInd
                
        return res