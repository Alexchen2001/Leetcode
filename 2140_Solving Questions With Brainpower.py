class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dp(index):

            # to stop when questions goes out of bound base case
            if index >= len(questions):
                return 0
            
            # currIndex + how many questions needed to skip + 1(to land on the next ques)
            nextQ = index + questions[index][1] + 1

            # case 1: solve all questions that can solved
            # case 2: skip current solve next
            return max(questions[index][0] + dp(nextQ), dp(index + 1))
        
        return dp(0)