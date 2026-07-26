class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open_closed={"}":"{",")":"(","]":"["}
        for bracket in s:
            if bracket in open_closed:
                if stack and stack[-1]== open_closed[bracket]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(bracket)
        return True if not stack else False