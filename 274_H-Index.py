class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def check(citation):
            count = 0
            for paper in citations:
                if paper >= citation:
                    count += 1
            
            return count >= citation
                
        
        low = 0
        high = len(citations)
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1
        return low - 1

    