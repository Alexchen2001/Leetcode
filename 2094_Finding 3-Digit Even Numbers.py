from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = permutations(digits, 3)
        visited = set()
        resArr = []
        for i in res:
            if i[0] != 0 and i[2] % 2 == 0:
                ans = int(str(i[0]) + str(i[1])+str(i[2]))
                if ans not in visited:
                    visited.add(ans)
                    resArr.append(ans)
        resArr.sort()
        return resArr
        
        
