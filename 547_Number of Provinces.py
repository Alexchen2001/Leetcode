class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        province = 0

        def dfs(isConnected, currNum):
            nonlocal seen

            if currNum in seen:
                return 0
            
            seen.add(currNum)
            for j in range(len(isConnected)):
                if isConnected[currNum][j] == 1:
                    dfs(isConnected, j)
            
        
        for i in range(len(isConnected)):
            if i not in seen:
                province += 1
            dfs(isConnected, i)
        
        return province 

