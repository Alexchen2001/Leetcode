class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set() 
        
        def dfs(keys):
            nonlocal visited
            nonlocal rooms

            for key in keys:
                if key not in visited:
                    visited.add(key)
                    dfs(rooms[key])



        visited.add(0)
        dfs(rooms[0])


        if len(visited) == len(rooms):
            return True
        else:
            return False 