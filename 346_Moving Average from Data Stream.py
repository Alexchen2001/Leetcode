class MovingAverage:

    def __init__(self, size: int):
        ## initiallizing a queue from collections module where 
        ## it has a max legnth of the given size (sliding window)
        self.queue = collections.deque(maxlen = size)

    def next(self, val: int) -> float:
        ## if the queue is full (based on size) it pops from the left 
        ## find the average through division
        self.queue.append(val)
        return sum(self.queue)/len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)