from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: [[],[]])
        # red : 0
        # blue: 1

        red = 0
        blue = 1
        for [a,b] in redEdges:
            graph[a][red].append(b)
        
        for [c,d] in blueEdges:
            graph[c][blue].append(d)
        
        ans = [float("inf")] * n
        queue = deque([(0,red,0),(0,blue,0)]) # node, color, steps
        visited = set()

        while queue:
            (node,color,steps) = queue.popleft()
            ans[node] = min(ans[node], steps)

            for nextNode in graph[node][color]:
                if (nextNode,1 - color) not in visited:
                    visited.add((nextNode, 1 - color))
                    queue.append((nextNode,1 - color, steps + 1))
        
        for i in range (n):
            if ans[i] == float("inf"):
                ans[i] = -1
        
        return ans

        
        