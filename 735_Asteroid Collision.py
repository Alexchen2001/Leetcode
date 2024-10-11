from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque([])
        n = len(asteroids)
        for i in range(n):
            while stack and (asteroids[i] < 0 and stack[-1]> 0):
                if abs(asteroids[i]) < abs(stack[-1]):
                    break
                elif abs(asteroids[i]) > abs(stack[-1]):
                    stack.pop()
                    continue
                else:
                    stack.pop()
                    break
            else:
                stack.append(asteroids[i])
        
        return list(stack)