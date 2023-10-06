class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        ## Use two pointer Approach
        lw = 0
        hi = len(s) -1
        
        while lw < hi:
            temp = s[hi]
            s[hi] = s[lw]
            s[lw] = temp
            lw += 1
            hi -= 1
            
        return s
        
        

        