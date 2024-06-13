from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        #establish a queue, appending the initial node
        queue = deque([[root]])

        # initiate a result array to store all max variable from each level
        res = []

        ## continuously runs if queue stills has something
        while queue:
            # pops the level as a list of nodes
            nodes = queue.popleft()
            
            # intiiates an array for every iteration to 
            # coolect the nodes for next level and the values
            # of current level
            currLevVals = []
            nextLevel = []

            # iterates throught current level 
            for node in nodes:
                # only deal with it if it is not a null node
                if node is not None:
                    currLevVals.append(node.val)
                    if node.left:
                        nextLevel.append(node.left)
                    if node.right:
                        nextLevel.append(node.right)
            
            # only append if there is a value in the array
            if (currLevVals != []):
                res.append(max(currLevVals))
            #breaks the while loop if there is no next levels
            if (nextLevel == []):
                break

            # puts the next level to be iterated through
            queue.append(nextLevel)

        return res


            
        
        