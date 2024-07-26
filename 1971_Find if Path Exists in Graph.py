class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        routes = defaultdict(list)
        for nodeA, nodeB in edges:
            routes[nodeA].append(nodeB)
            routes[nodeB].append(nodeA)

        def dfs(node):
            nonlocal routes
            nonlocal visited
            nonlocal destination
            
            if node == destination:
                return True
            visited.add(node)
            for nextNode in routes[node]:
                if nextNode not in visited:
                    if dfs(nextNode):
                        return True

        
        visited.add(source)
        
        if dfs(source):
            return True
        return False
