class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## Note: during the iteration of the dictioanry, it might only apply to 
        ## cases where there is exactly one solution, since dicitonary can 
        ##not  possess same key, along that during the iteration it does not 
        ## contain all element until the last iteration.
        
        ## creates a dictionary an find out the num of 
        ##elements in the nums list
        numMaps = {}
        amt = len(nums)

        ## iterate through amount of element in list
        for i in range(amt):
            ## finds the complement of the current element from target
            req = target - nums[i]
            ## using dictionary, if the complement is in the dictionary, 
            ## it retreieveds the index of complement stored in dictionary 
            ##and the current index "i"
            if req in numMaps:
                return [numMaps[req],i]
            ## stores the num element into the dictionary as key  and stores the         ## the index as the value
            numMaps[nums[i]] = i
        ## No solution returns empty list
        return []


            

