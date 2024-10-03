class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answers = [1] * n

        prefixProduct = 1
        for i in range(n):
            answers[i] = prefixProduct
            prefixProduct *= nums[i]
        
        suffixProduct = 1
        for j in range(n - 1, -1, -1):
            answers[j] *= suffixProduct
            suffixProduct *= nums[j]
        return answers


            
            
