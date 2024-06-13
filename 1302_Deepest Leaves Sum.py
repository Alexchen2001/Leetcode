from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # initialized a queue with initial node
        # initialized a result, and a list for the values of last level
        queue = deque([[root]])
        res= 0
        lastValsList = []

        #iterates when there is something in queue
        while queue:
            # provised the current level of nodes, a list of node
            # initiate a list to find next level
            nodes = queue.popleft()
            nextLevel = []

            # iterates in the list of nodes
            for node in nodes:
                #stores the value of this current level
                lastValsList.append(node.val)
                # ignores null nodes
                if node is not None:
                    if node.left:
                        nextLevel.append(node.left)

                    if node.right:
                        nextLevel.append(node.right)
            
            ## only append into queue if it is not the end of the tree levels
            ## if it is the end of the level, add the values for sum of the last level
            if nextLevel != []:
                queue.append(nextLevel)
            else:
                res = sum(lastValsList)
                break
            # since it is not last level, we do not need it
            lastValsList = []
        return res
            


        