class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        count = 0
        currMap= {}
        directedRoute = set()
        visited = set()
        visited.add(0)
        
        # utilized dictionary to preprocess the treeGraph of the cities
        # making it undirected edge
        # also keeps the original directed edge in a set
        for city1, city2 in connections:
            if city1 not in currMap:
                currMap[city1] = []
            if city2 not in currMap:
                currMap[city2] = []
            currMap[city1].append(city2)
            currMap[city2].append(city1)
            directedRoute.add((city1,city2))

        # The DFS algo goes thorugh form the root of the graph City "0"     
        def dfs(city):
            nonlocal count
            nonlocal currMap
            nonlocal directedRoute
            nonlocal visited

            # checks in all cities that is connected to the city
            for connectedCity in currMap[city]:
                ### if we never check that city, that means we have not counted the change
                ###so go in and change them
                if connectedCity not in visited:
                    # if the city is not in the direction of going to city"0" 
                    #need to change so add 1
                    if (city,connectedCity) in directedRoute:
                        count += 1
                    # after manipulating the city add it into changed list
                    # so we don't duplicate count it
                    visited.add(connectedCity)
                    # recursively goes through city that is connected to the given city
                    dfs(connectedCity)

        dfs(0)
        return count

