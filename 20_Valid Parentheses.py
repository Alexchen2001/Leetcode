class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbolDict = {"{":"}", "(":")", "[":"]"}

        ## Iterates over the string by characters
        for i in s:
            ##Appends into the stack if it is an opening bracket
            if i in symbolDict.keys():
                stack.append(i)
            else:
                ## if there is nothing in stack but there is a closing bracket
                ## then it is false (edge case)
                if not stack:
                    return False

                ## Checks whether if the symbol matches the opening bracket
                previousSymbol = stack.pop()
                if symbolDict[previousSymbol] != i:
                    return False
            
        ## if it is empty then it would be true
        return not stack
        