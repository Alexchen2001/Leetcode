# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        arr.append(root.val)
        def dfs(root):
            if not root:
                return 0
            
            if root.val != None:
                if root.left:
                    arr.append(root.left.val)
                    dfs(root.left)
                if root.right:
                    arr.append(root.right.val)
                    dfs(root.right)
        dfs(root)
        print(arr)
        arr.sort(reverse = True)
        print(arr)
        minDiff = 9999999999
        for i in range(len(arr) - 1):
            minDiff = min(minDiff, abs(arr[i] - arr[i+1]))

        return minDiff
            


        