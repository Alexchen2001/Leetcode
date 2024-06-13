from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([[root]])
        res = []

        while queue:
            nodes = queue.popleft()
            
            if len(nodes) == 0 or nodes[0] is None:
                break
            
            res.append(nodes[-1].val)
            nextLayer  = []
            for node in nodes:
                if node.left:
                    nextLayer.append(node.left)
                if node.right:
                    nextLayer.append(node.right)
            queue.append(nextLayer)

        return res

        
        
        # queue = deque([[root]])
        # res = []
        # while queue:
        #     nodes = queue.popleft()
        #     print(nodes)
        #     if len(nodes) == 0 or nodes[0] is None:
        #         break
        #     res.append(nodes[-1].val)
        #     next_level = []
        #     for node in nodes:
        #         if node is not None:
        #             if node.left is not None:
        #                 next_level.append(node.left)
        #             if node.right is not None:
        #                 next_level.append(node.right)
        #     if len(next_level) > 0:
        #         queue.append(next_level)                

        # return res

        