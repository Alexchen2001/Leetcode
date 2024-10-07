class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        setHave = set()
        frequency = {}
        count = 0
        n = len(grid)

        for i in range(n):
            element = tuple(grid[i])
            setHave.add(element)
            if element not in frequency:
                frequency[element] = 1
            else:
                frequency[element] += 1
        
        for j in range(n):
            arr = []
            for k in range(n):
                arr.append(grid[k][j])
            
            temp = tuple(arr)
            if temp in setHave:
                count += frequency[temp]
        return count




