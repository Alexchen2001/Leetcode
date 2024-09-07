class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []

        def backtrack(currArr, currNode, NodePath):
            if currNode == len(graph) - 1:
                ans.append(currArr[:])
                return
            
            for node in NodePath:
                currArr.append(node)
                backtrack(currArr, node, graph[node])
                currArr.pop()
            
        backtrack([0], 0, graph[0])
        return ans
        