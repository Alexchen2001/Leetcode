class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ##Restriction: array has to be initially sorted.
        n = len(nums) ## checks for the length of array
        result = [0] * n
        ## initiation of the two pointer 
        ## left traverses through negative num 
        ## right traverses backward from positive number
        left = 0 
        right = n -1
        ## for loops that iterates down until it reaches -1
        ## puthon for loop range(start, stop, step)
        for i in range(n -1, -1, -1):
            ## we loop for the largest element first
            if abs(nums[left])< abs(nums[right]):
                ## the right is the larget initial positive integer (last element of 
                ## positive integer)
                square = nums[right]
                right -= 1
            else:
                ## the left is the smallest number (negative number), but will 
                ## be the largest after squareing, so the first element of the array
                square = nums[left]
                left += 1
            result[i] = square * square
        return result
        