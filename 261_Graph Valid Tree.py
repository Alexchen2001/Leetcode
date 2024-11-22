from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n -1:
            return False
        
        visited = set()
        graph = {}
        for i in range(n):
            graph[i] = []
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        queue = deque([0])
        visited.add(0)
        while queue:
            qLen = len(queue)
            for _ in range(qLen):
                currNode = queue.popleft()
                for nextNode in graph[currNode]:
                    if nextNode not in visited:
                        queue.append(nextNode)
                        visited.add(nextNode)
        
        if len(visited) < n:
            return False
        return True


        

        
