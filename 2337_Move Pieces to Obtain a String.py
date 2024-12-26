class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)

        str1 = ""
        str2 = ""
        
        startPtr = 0

        for b in range(n):
            if target[b] != "_":
                str1 = str1 + target[b]
                while startPtr < n and start[startPtr]  == "_":
                    startPtr += 1
                
                if startPtr < n and target[b] == start[startPtr]:
                    if target[b] == "R":
                        if startPtr > b:
                            return False
                        
                    if target[b] == "L":
                        if startPtr < b:
                            return False
                    startPtr += 1
                else:
                    return False
        for a in range(n):
            if start[a] != "_":
                str2 = str2 + start[a]
        if str1 != str2:
            return False
        return True
            


        

        
