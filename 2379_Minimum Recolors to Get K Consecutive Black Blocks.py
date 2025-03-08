class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        start = 0
        n = len(blocks)
        minOp = 0
        currOp = 0
        for i in range(k):
            if blocks[i] == "W": 
                currOp += 1
        minOp = currOp
        for end in range(k, n):
            if blocks[end] == "W":
                currOp += 1
            if blocks[start] == "W":
                currOp -= 1
            start += 1
            minOp = min(minOp,currOp)
        
        return minOp
        




