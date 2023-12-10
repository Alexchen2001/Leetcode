class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
         
        result = []
        for j in range(len(variables)):
            a = variables[j][0]
            b = variables[j][1]
            c = variables[j][2]
            m = variables[j][3]
            if(((((a**b) % 10)**c) % m) == target):
                result.append(j)
        
        return result
            