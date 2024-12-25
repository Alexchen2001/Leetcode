class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        ndict = {}
        n = len(arr)

        for i in range(n):
            if arr[i] not in ndict:
                ndict[arr[i]] = i
        
        for j in range(n):
            temp = arr[j] * 2

            if temp in ndict:
                if ndict[temp] != j:
                    return True
        return False


        