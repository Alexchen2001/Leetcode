class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        nums1Length = len(nums1)
        nums2Length = len(nums2)
        @cache
        def dp(currIndex, currJdex):
            if currIndex == nums1Length or currJdex == nums2Length:
                return 0
            

            res = float('-inf')
            if nums1[currIndex] == nums2[currJdex]:
                res = max(res, 1 + dp(currIndex + 1, currJdex + 1))
            else:
                res = max(res, dp(currIndex + 1, currJdex), dp(currIndex, currJdex + 1), dp(currIndex + 1, currJdex + 1))
            return res


        return dp(0,0)

