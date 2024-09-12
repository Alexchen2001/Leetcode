class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        currPos = (0,0)
        visited.add((0,0))
        for i in range(len(path)):
            if path[i] == "N":
                currPos = (currPos[0],currPos[1] + 1)
            elif path[i] == "S":
                currPos = (currPos[0],currPos[1] - 1)
            elif path[i] == "E":
                currPos = (currPos[0] + 1,currPos[1])
            elif path[i] == "W":
                currPos = (currPos[0] - 1,currPos[1])
            
            if currPos not in visited:
                visited.add(currPos)
            else:
                return True
        return False

        