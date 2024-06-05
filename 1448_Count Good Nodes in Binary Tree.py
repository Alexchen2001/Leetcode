# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root,highestVal):
            nonlocal count
            if not root:
                return 0
            currHigh = highestVal
            print('Im here')
            if (root.val >= highestVal):
                count += 1
                currHigh = root.val

            leftTraverse = dfs(root.left,currHigh)
            rightTraverse = dfs(root.right,currHigh)


        dfs(root,float('-inf'))
        return count

        