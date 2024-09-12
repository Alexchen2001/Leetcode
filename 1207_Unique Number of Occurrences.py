class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}

        for num in arr:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        

        visited = set()
        for key, value in dict.items():
            if value not in visited:
                visited.add(value)
            else:
                return False
        return True
