# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val
        prevDiff = abs(root.val - target)
        def findsIt(node):
            nonlocal target
            nonlocal res
            nonlocal prevDiff
            
            if not node:
                return 0
            if node.val != None:
                if target <= node.val:
                    if abs(target - node.val) < prevDiff:
                        res = node.val
                        prevDiff = abs(target - node.val)
                    findsIt(node.left)
                elif target >= node.val:
                    if abs(target - node.val) <= prevDiff:
                        res = node.val
                        prevDiff = abs(target - node.val)
                    findsIt(node.right)
                else:
                    return 0
        findsIt(root)
        return res