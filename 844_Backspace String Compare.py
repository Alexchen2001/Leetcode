class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        stack1 = []
        ## iteractes through every character
        for i in s:
            ## if not empty and backspace
            if stack and i == '#':
                stack.pop()
            ## only append if it is not a backspace
            elif i != '#':
                stack.append(i)
        ## reference top one same logic
        for j in t:
            if stack1 and j == '#':
                stack1.pop()
            elif j != '#':
                stack1.append(j)
        ## Inner function way also works but too slow
        # def strCheck(givenStr:str, stak:list):
        #     for i in givenStr:
        #         if stak and i == '#':
        #             stak.pop()
        #         elif i != '#':
        #             stak.append(i)
        # strCheck(s,stack)
        # strCheck(t,stack1)
        ## if both are the same its true otherwise false
        if ("".join(stack) == "".join(stack1)):
            return True
        return False


        