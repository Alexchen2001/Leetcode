class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dict = {}

        for num in arr:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        luckyNum = -1
        for key,value in dict.items():
            if key == value:
                if luckyNum < key:
                    luckyNum = key
        
        return luckyNum