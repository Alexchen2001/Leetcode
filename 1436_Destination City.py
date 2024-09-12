from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        visited = set()
        reached = set()

        for cityA, cityB in paths:
            visited.add(cityA)
            reached.add(cityB)
        
        return reached.difference(visited).pop()

