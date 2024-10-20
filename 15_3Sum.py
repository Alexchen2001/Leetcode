
## AC Solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        fDict = {}
        visited = set()
        res = []

        for num in nums:
            if num not in fDict:
                fDict[num] = 1
            else:
                fDict[num] += 1
        keys = fDict.keys()
        for key in keys:
            for key2 in keys:
                compliment = 0 - (key + key2)
                if compliment in fDict:
                    if key <= key2 <= compliment:
                        if key == key2 and key2 == compliment:
                            
                            if fDict[compliment] >= 3 and (compliment,compliment, compliment) not in visited:
                                res.append([compliment,compliment, compliment])
                                visited.add((compliment,compliment,compliment))
                        elif key == key2 or key2 == compliment:
                            temp = tuple(sorted([key,key2, compliment]))
                            if key == key2:
                                if fDict[key] >= 2:
                                   if temp not in visited:
                                        res.append([key,key2, compliment])
                                        visited.add(temp)
                            else:
                                if fDict[key2] >= 2:
                                    if temp not in visited:
                                        res.append([key,key2, compliment])
                                        visited.add(temp)
                        else:
                            temp = tuple(sorted([key,key2, compliment]))
                            if temp not in visited:
                                res.append([key,key2, compliment])
                                visited.add(temp)
        return res







## Bulr Solution  
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        fDict = {}
        for num in nums:
            if num not in fDict:
                fDict[num] = 1
            else:
                fDict[num] += 1
        if 0 in fDict:
            if fDict[0] >= 3:
                res.append([0,0,0])
        keys = fDict.keys()
        for key in keys:
            if fDict[key] >= 2:
                compliment = 0 - (key * 2)
                if compliment > key:
                    if compliment in keys:
                        res.append([key,key, compliment])
            for key2 in keys:
                if key2 > key:
                    compliment = 0 - (key2 + key)
                    if compliment >= key2:
                        if compliment == key2 or compliment == key:
                            if fDict[compliment] >= 2:
                                res.append([key, key2, compliment])
                        
                        else:
                            if compliment in fDict:
                                res.append([key, key2, compliment])
                        
        return res
