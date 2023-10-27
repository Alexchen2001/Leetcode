class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        ## create a dictionary
        dic = {}
        ## create the invalid result
        ans = -1
        
        ## add all element: frequency to dictionary
        for i in nums:
            if i not in dic: 
                dic[i] = 1
            else:
                dic[i] += 1
                
        ## sort the dictionary base of dictionary key (element)
        sortedDic = dict(sorted(dic.items(), reverse = True))
        
        ## finds the first occurrence of the largest key that only occurred once
        for j in sortedDic:
            if (sortedDic[j]  > 1):
                continue
            else:
                ans = j
                break
        return ans
                