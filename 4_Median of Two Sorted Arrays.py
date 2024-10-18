import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        res = 0
        if m == 0 and n == 0:
            return 0
        totalLength = m + n
        medianIndexCount = None
        isEven = False
        if totalLength % 2 == 0:
            isEven = True
            medianIndexCount = totalLength / 2
        else:
            medianIndexCount = math.ceil(totalLength / 2)

        count = 1
        left = 0
        right = 0
        while count <= medianIndexCount:
            temp  = None
            if left < m and right < n:
                if nums1[left] <= nums2[right]:
                    temp = nums1[left]
                    left += 1
                else:
                    temp = nums2[right]
                    right += 1
            elif left < m and right >= n:
                temp = nums1[left]
                left += 1
            
            elif left >= m and right < n:
                temp = nums2[right]
                right += 1

            if count == medianIndexCount:
                res = temp
            count += 1
        
        if not isEven:
            return float(res)
        else:
            if left < m and right < n:
                if nums1[left] <= nums2[right]:
                    res = res + nums1[left]
                else:
                    res = res + nums2[right]
            elif left < m and right >= n:
                res = res + nums1[left]
            
            elif left >= m and right < n:
                res = res + nums2[right]
            
            return res /2
        
            
            