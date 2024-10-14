from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        catalog = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses

        for course, preReq in prerequisites:
            catalog[preReq].append(course)
            inDegree[course] += 1

        queue = deque([index for index in range(numCourses) if inDegree[index] == 0])
        visited = 0 
        while queue:
            currPreReq = queue.popleft()
            visited += 1
            for linkedCourse in catalog[currPreReq]:
                inDegree[linkedCourse] -= 1

                if inDegree[linkedCourse] == 0:
                    queue.append(linkedCourse)
            
        return visited == numCourses

                

        
