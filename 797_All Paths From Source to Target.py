class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []

        def backtrack(currArr, currNode):
            if currNode == len(graph) - 1:
                ans.append(currArr[:])
                return
            
            for node in graph[currNode]:
                currArr.append(node)
                backtrack(currArr, node)
                currArr.pop()
            
        backtrack([0], 0)
        return ans
        