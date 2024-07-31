# Version 3 Most efficient (removing unneeded condition checks)
# based on data preprocessing so restricted nodes are excluded anyway, so 
# no need to check
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        visited = set()
        restrictedSet = set(restricted)
        daTree = defaultdict(list)
        result = 1
        

        for a,b in edges:
            if a not in restrictedSet and b not in restrictedSet:
                daTree[a].append(b)
                daTree[b].append(a)

        def dfs (node):
            nonlocal daTree
            nonlocal restricted
            nonlocal visited
            nonlocal result

            if node not in visited :
                result += 1
            visited.add(node)
            for currNode in daTree[node]:
                if currNode not in visited :
                    dfs(currNode)

        
        visited.add(0)
        dfs(0)

        return result


# Version 2 (exclusion: exclude restricted nodes, less space and time complexity)
# class Solution:
#     def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
#         visited = set()
#         restrictedSet = set(restricted)
#         daTree = defaultdict(list)
#         result = 1
        

#         for a,b in edges:
#             if a not in restrictedSet and b not in restrictedSet:
#                 daTree[a].append(b)
#                 daTree[b].append(a)

#         def dfs (node):
#             nonlocal daTree
#             nonlocal restricted
#             nonlocal visited
#             nonlocal result

#             if node not in visited and node not in restrictedSet:
#                 result += 1
#             visited.add(node)
#             for currNode in daTree[node]:
#                 if currNode not in visited and node not in restrictedSet:
#                     dfs(currNode)

        
#         visited.add(0)
#         dfs(0)

#         return result



# Version 3 (Data structure/store change array to set, less time complexity for compairson)
# class Solution:
#     def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
#         visited = set()
#         restrictedSet = set(restricted)
#         daTree = defaultdict(list)
#         result = 1
        

#         for a,b in edges:
#             daTree[a].append(b)
#             daTree[b].append(a)

#         def dfs (node):
#             nonlocal daTree
#             nonlocal restricted
#             nonlocal visited
#             nonlocal result

#             if node not in visited and node not in restrictedSet:
#                 result += 1
#             visited.add(node)
#             for currNode in daTree[node]:
#                 if currNode not in visited and node not in restrictedSet:
#                     dfs(currNode)

        
#         visited.add(0)
#         dfs(0)

#         return result


