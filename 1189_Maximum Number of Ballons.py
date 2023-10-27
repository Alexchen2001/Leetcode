class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ## create a hashtable for known letter count required for "balloon"
        dic1 = {"b": 1, "a": 1, "l":2, "o":2, "n": 1}
       
        ## created empy dictionary for the frequency of letter in given input
        dic = {}
        
        ## created an array that stores the amount of set of letter we have
        arr = []
        count = 0
        
        ## iterates and parses the frequency for the given input into dictionary
        for i in range(len(text)):
            if (text[i] not in dic):
                dic[text[i]] = 1
            else:
                dic[text[i]] += 1
        
        ## finds the amount of set of the letters that we can obtain
        ## if one letter is not found in the input dictionary, then we cannot
        ## form the word so return 0 immediately
        for i in dic1:
            if ( i in dic):
                arr.append(dic[i] // dic1[i])
            else:
                return 0
        ## the possiblity to form a word is to have all element
        ## so it should be the letter that has the minimal set available,
        ##Since we can't miss a letter
        return min(arr)