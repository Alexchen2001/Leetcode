class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        if n < 1: 
            return True
        intervals.sort(key = lambda x : [x[0],x[1]])

        [start, end] = intervals[0]

        for i in range(1, n):
            if intervals[i][0] >= start and  intervals[i][0] < end:
                return False
            
            if intervals[i][1] > start and intervals[i][1] <= end:
                return False
            
            if intervals[i][1] > end:
                end = intervals[i][1]
        return True
            