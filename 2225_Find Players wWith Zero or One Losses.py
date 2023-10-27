from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ## initiate an dictionary that accepts only initiate values of a key in format of
        ##[0,0]
        count = defaultdict(lambda:[0,0])
        for i in matches:
            ## format [wins, loss]
            ## dict[key][0] is wins of the key 
            ## dict[key[1] is the loss of the key]
            count[i[0]][0] += 1
            count[i[1]][1] += 1
        ans = [[],[]]
        
        ## this for loop j provides the keys in count dict
        for j in count:
            
            ## since in this dict the format is [0,0],
            ## the way to access is dict[key][element of the list]
            if (count[j][1] == 0 ) :
                ans[0].append(j)
            elif (count[j][1] == 1):
                ans[1].append(j)
            else:
                continue
        
        ## required sorted for this problem
        ans[0].sort()
        ans[1].sort()
        return ans
        
        