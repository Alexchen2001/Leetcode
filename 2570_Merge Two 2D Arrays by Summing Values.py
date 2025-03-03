class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        len1 = len(nums1)
        len2 = len(nums2)
        ptr1 = 0
        ptr2 = 0
        dictA = {}

        def addToDict(id, val):
            if id not in dictA:
                dictA[id] = val
            else:
                dictA[id] += val
        while ptr1 < len1 or ptr2 < len2:
            if ptr1 < len1 and ptr2 < len2:
                if nums1[ptr1][0] == nums2[ptr2][0]:
                    temp = nums1[ptr1][1] + nums2[ptr2][1]
                    addToDict(nums1[ptr1][0],temp)
                    ptr1 += 1
                    ptr2 += 1
                elif nums1[ptr1][0] < nums2[ptr2][0]:
                    addToDict(nums1[ptr1][0],nums1[ptr1][1])
                    ptr1 += 1
                else:
                    addToDict(nums2[ptr2][0],nums2[ptr2][1])
                    ptr2 += 1
            elif ptr1 < len1 and ptr2 >= len2:
                addToDict(nums1[ptr1][0],nums1[ptr1][1])
                ptr1 += 1
            elif ptr2 < len2 and ptr1 >= len1:
                addToDict(nums2[ptr2][0],nums2[ptr2][1])
                ptr2 += 1
            else:
                break
            
        res = [[id,val] for id,val in dictA.items()]
        return res