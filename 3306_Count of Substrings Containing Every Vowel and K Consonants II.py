class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        start = 0
        end = 0
        distV = {'a':0,'e':0,'i':0,'o':0,'u':0}
        con = 0
        ans = 0
        temp_count = 0
        left=0

        for char in word:
            if char in distV:
                distV[char]+=1
            else:
                con+=1
                temp_count=0
            
            while con>k:
                if word[left] in distV:
                    distV[word[left]]-=1
                else:
                    con-=1
                left+=1
            
            while con==k and min(distV.values())>=1:
                temp_count+=1
                if word[left] in distV:
                    distV[word[left]]-=1
                else:
                    con-=1
                left+=1
            
            ans+=temp_count
        
        return ans