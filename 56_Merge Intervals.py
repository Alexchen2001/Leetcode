class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(intervals)
        if n < 2:
            return intervals
        intervals.sort(key = lambda x: (x[0],x[1]))
        start, end= intervals[0][0], intervals[0][1]

        for i in range(1,n):
            if intervals[i][0] >= start and intervals[i][0] <= end:
                if intervals[i][1] > end:
                    end = intervals[i][1]    
            else:
                res.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        res.append([start,end])

        return res


        

