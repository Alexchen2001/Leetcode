# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insertNode(node, val):
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    return 0
                insertNode(node.left,val)
            elif val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    return 0
                insertNode(node.right,val)
            else:
                return 0
        if not root:
            root = TreeNode(val)
        else:
            insertNode(root, val)
        return root




        