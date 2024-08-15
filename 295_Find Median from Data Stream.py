from heapq import * 
class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        
    def addNum(self, num: int) -> None:
        heappush(self.maxheap, - num)
        heappush(self.minheap, - heappop(self.maxheap))
        if len(self.minheap) > len(self.maxheap):
            heappush(self.maxheap, - heappop(self.minheap))
        


    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2
        elif len(self.maxheap) > len(self.minheap):
            return - self.maxheap[0]
        else:
            return self.minheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()