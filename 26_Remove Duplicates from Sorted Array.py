class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ## two pointer approach
        ## Imagine using this example
        ## arr = [1,2,2,3,4]
        ## index  0,1,2,3,4
        ## the conecpt idea is that the i pointer checks for duplicates
        ## the j stays as a pointer where it stops as the last place that did not duplicate
        ## if seen a duplicate the j is where the preceeding of the non-duplicate delemtn would 
        ##land. At the end is how many element the array should have
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

        
        