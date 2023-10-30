class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        ans = 0
        
        ## create a set where the distinct category of stones are stored.
        visit = set()
        for i in jewels:
            visit.add(i)
            
        ## counts the stones that you possess that are jewels
        for j in stones:
            if j in visit:
                ans += 1
            else:
                continue
        return ans
            
        