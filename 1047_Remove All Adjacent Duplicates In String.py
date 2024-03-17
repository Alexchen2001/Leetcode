class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        ## iteraes through the string by characters
        for i in s:
            ##edge case: if empty append it
            if not stack :
                stack.append(i)
            elif stack[-1] == i:
                ## remove of the stack only if it is matching, meaning no going to be appened
                stack.pop()
            else:
                ## if is not empty and not matching append it
                stack.append(i)
        ## appends all character remining in stack
        return "".join(stack)
        