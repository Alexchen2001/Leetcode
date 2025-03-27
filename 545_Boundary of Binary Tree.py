# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        leftB = []
        rightB = []
        leafs = []
        if not root.left and not root.right:
            return [root.val]
        def dfsLeft(node):
            nonlocal leftB
            if not node or (not node.left and not node.right):
                return 
            leftB.append(node.val)
            if node.left:
                dfsLeft(node.left)
            
            else:
                dfsLeft(node.right)
            return 
            
        def dfsRight(node):
            nonlocal rightB

            if not node or (not node.left and not node.right):
                return 
            if node.right:
                dfsRight(node.right)
            
            else:
                dfsRight(node.left)
            rightB.append(node.val)

            return 

        def dfsLeaf(node):
            nonlocal leafs
            if not node:
                return 
            if not node.left and not node.right:
                leafs.append(node.val)
                return 
            if node.left:
                dfsLeaf(node.left)
            
            if node.right:
                dfsLeaf(node.right)
            return 
        dfsLeft(root.left)
        dfsRight(root.right)
        dfsLeaf(root)
        return [root.val] + leftB + leafs + rightB

        



