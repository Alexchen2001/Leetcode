class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(index, takenFirst, takenPrev):
            if index == n:
                return 0
            
            # check for limitation 
            # last index, whether if robbed first house, and not taking the previous element
            if index == n -1 and takenFirst and not takenPrev:
                return dp(index + 1, takenFirst, False)
            # skip 
            ans = dp(index + 1, takenFirst, False)
            if not takenPrev:
                newTakenFirst = takenFirst
                if index == 0:
                    newTakenFirst = True
                ans = max(ans, nums[index] + dp(index + 1, newTakenFirst, True))
            return ans
        return dp(0, False, False)

            


            

        