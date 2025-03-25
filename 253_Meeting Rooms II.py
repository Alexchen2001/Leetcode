class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n < 1:
            return 0
        if n == 1:
            return 1
        
        intervals.sort(key = lambda x: x[0])
        currRooms = []
        heapq.heappush(currRooms, intervals[0][1])

        for meetTime in intervals[1:]:
            if meetTime[0] >= currRooms[0]:
                heapq.heappop(currRooms)
                heapq.heappush(currRooms, meetTime[1])
            else:
                heapq.heappush(currRooms, meetTime[1])
        
        return len(currRooms)


