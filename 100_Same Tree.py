# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Checks if both is null then true
        if not p and not q:
            return True
        
        # if one returns different it would give False
        # since if both is true it would return in first condition
        if not p or not q:
            return False
        # value have to match
        if p.val != q.val:
            return False
        #keep traversing
        leftTraverse = self.isSameTree(p.left,q.left)
        rightTraverse = self.isSameTree(p.right,q.right)
        return leftTraverse and rightTraverse
        '''
        Wrong way
        result1 = []
        result2 = []

        def inOrder(root,result):
            if not root:
                return 0

            inOrder(root.left,result)
            result.append(root.val)
            inOrder(root.right,result)

        
        inOrder(p,result1)
        inOrder(q,result2)

        return result1 == result2
        '''

        