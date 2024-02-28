class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ## append everything to the ending of nums1
        ## then sort
        ## since appending is just the length of the nums 2 it is constant time
        ## and using a sort function is n log n, so it is still
        ## relative fast and acceptable
        for i in range(len(nums2)):
            nums1[- (i+1)] = nums2[i]
        nums1.sort()
     
        