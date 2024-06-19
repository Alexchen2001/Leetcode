# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        seq = []

        def inOrderTraversal(root):
            if not root:
                return 0
            
            inOrderTraversal(root.left)
            seq.append(root.val)
            inOrderTraversal(root.right)
        
        inOrderTraversal(root)

        for i in range(len(seq) - 1):
            if seq[i] >= seq[i + 1]:
                return False
        
        return True
        
        