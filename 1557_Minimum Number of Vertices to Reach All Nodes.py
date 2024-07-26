class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = [0] * n
        for _ , to in edges:
            indegrees[to] += 1
        return [vertice for vertice in range(n) if indegrees[vertice] == 0]
        