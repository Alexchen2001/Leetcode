from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = defaultdict(int)
        ans = 0
        ## keeping lw and "i" as the two pointers
        lw = 0
        ##dictionary format letter (key) : index (value)
        for i in range(len(s)):
            ## base case: adds non-existent element into dictionary
            if s[i] not in visited:
                visited[s[i]] = i
            ##if it is in there, then move to the next element and reintiate
            ## the lw pointer to the next element.
            ## if there the pointer is above the repeated index, just re-initiate
            else: 
                if (lw > visited[s[i]]):
                    visited[s[i] ] = i
                else:
                    lw = visited.pop(s[i]) +1
                    visited[s[i]] = i
            
                
                
            ans = max(ans, i - lw + 1)
            
        return ans
            