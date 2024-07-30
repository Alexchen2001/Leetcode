class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        path = defaultdict(list)
        visited = set()
        result = 0

        for a,b in edges:
            path[a].append(b)
            path[b].append(a)
        
        if len(path) != n:
            for i in range(n):
                if i not in path.keys():
                    path[i] = []
        
        def travel(gInput):
            nonlocal path
            nonlocal visited
            
            visited.add(gInput)
            for node in path[gInput]:
                if node not in visited:
                    travel(node)

            
        
        for j in range(n):
            if j not in visited:
                travel(j)
                result += 1
        return result



        