from heapq import heappush, heappop
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = []
        available = []
        dictF = {}
        for i in range(n):
            heappush(available, i)
            dictF[i] = 0
        
        meetings.sort(key = lambda x:x[0])
        
        for meeting in meetings:
            start, end = meeting[0],meeting[1]
            while rooms and rooms[0][0] <= start:
                _, room = heappop(rooms)
                heappush(available, room)
            if available:
                roomNumber = heappop(available)
                endTime = end
                dictF[roomNumber] += 1
                heappush(rooms, (endTime,roomNumber))
            else:
                (endTime,roomNumber) = heappop(rooms)
                duration = end - start
                endTime += duration
                dictF[roomNumber] += 1
                heappush(rooms, (endTime,roomNumber))
        
        res = [(roomNum,frequency) for roomNum,frequency in dictF.items()]
        res.sort(key = lambda x: (-x[1],x[0]))
        print(res)
        return res[0][0]

