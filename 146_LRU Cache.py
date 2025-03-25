class LRUCache:
    class Node:
        def __init__(self,key, value,prev, next):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.currSize = 0
        self.Head = self.Node(-1,-1, None, None)
        self.Tail = self.Node(-1,-1, self.Head,None)
        self.Head.next = self.Tail
        self.LRU = {}

    def _update(self, key):
        self.LRU[key].prev.next = self.LRU[key].next
        self.LRU[key].next.prev = self.LRU[key].prev
        self.Tail.prev.next = self.LRU[key]
        self.LRU[key].prev = self.Tail.prev
        self.Tail.prev = self.LRU[key]
        self.LRU[key].next = self.Tail
    def get(self, key: int) -> int:
        if key in self.LRU:
            self._update(key)
            return self.LRU[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.LRU:
            self._update(key)
            self.LRU[key].value = value
        else:
            if self.capacity == self.currSize:
                lruKey = self.Head.next.key
                self.Head.next = self.Head.next.next
                self.Head.next.prev = self.Head
                self.LRU.pop(lruKey)
                self.currSize -= 1
            self.LRU[key] = self.Node(key, value, self.Tail.prev,self.Tail)
            self.Tail.prev.next = self.LRU[key]
            self.Tail.prev = self.LRU[key]
            self.currSize += 1
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)