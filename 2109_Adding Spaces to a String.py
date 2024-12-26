class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr = []
        currI = 0
        n = len(s)
        for i in range(n):
            if currI < len(spaces):
                if i != spaces[currI]:
                    arr.append(s[i])
                else:
                    arr.append(" ")
                    arr.append(s[i])
                    currI += 1
            else:
                arr.append(s[i:])
                break
        return ''.join(arr)
        