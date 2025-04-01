class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # nearest Candles to the left
        leftCandles = [-1] * n
        #nearest Candles from the right
        rightCandles = [-1] * n

        # How Many Plates at this position
        prefixPlates = [0] * (n + 1)

        for i in range(n):
            if s[i] == "*":
                prefixPlates[i + 1] = prefixPlates[i] + 1
            else:
                prefixPlates[i + 1] = prefixPlates[i]
        
        prev  = -1
        for i in range(n):
            if s[i] == "|":
                prev = i
            leftCandles[i] = prev
        
        next = -1
        for i in range(n -1, -1, -1):
            if s[i] == "|":
                next = i
            rightCandles[i] = next
        res = []
        
        for query in queries:
            lowB, highB = query
            # finds the index of the candle that is right of lower boundary
            lC = rightCandles[lowB]
            #finds the index of th candle that is left of the upper boundary
            rC = leftCandles[highB]
            if lC != -1 and rC != -1 and lC < rC:
                res.append(prefixPlates[rC] - prefixPlates[lC])
            else:
                res.append(0)
        return res






