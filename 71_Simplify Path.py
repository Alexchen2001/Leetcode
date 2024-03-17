class Solution:
    def simplifyPath(self, path: str) -> str:
        # splitting all string based upon "/"
        array = path.split("/")
        stack = []
        ## Iterating through the split elements
        for i in array:
            ## if the element is empty or current directory just proceed
            if i == "" or i == ".":
                continue
            ## if there is a directory in stack and it wants prev directory, pop it
            elif i == "..":
                if stack:
                    stack.pop()
            ## otherwise just keep appending
            else:
                stack.append(i)

        ## start with home directory"/", the join method only inserts the symbol between each 
        ## element
        return "/" + "/".join(stack)

        