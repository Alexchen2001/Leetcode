from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent):
            if not node:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node) 
        dfs(root, None)
        queue = deque([target])
        visited = {target}
        result = []
        distance  = 0

        while queue and k >= distance:
            qLength = len(queue)
            if k == distance:
                return [node.val for node in queue]
                
            for _ in range(qLength):
                currNode = queue.popleft()

                for neighbor in [currNode.left,currNode.right,currNode.parent]:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            distance += 1
        return []