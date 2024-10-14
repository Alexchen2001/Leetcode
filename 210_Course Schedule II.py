from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        catalog = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses

        for course, preReq in prerequisites:
            catalog[preReq].append(course)
            inDegree[course] += 1
        
        queue = deque([index for index in range(numCourses) if inDegree[index] == 0])
        visited = 0

        while queue:
            currPreReq = queue.popleft()
            res.append(currPreReq)
            visited += 1
            for nextCourse in catalog[currPreReq]:
                inDegree[nextCourse] -= 1
                if inDegree[nextCourse] == 0:
                    queue.append(nextCourse)
            
        
        if visited == numCourses:
            return res
        return []


