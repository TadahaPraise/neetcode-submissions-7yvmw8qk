class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for operator in tokens:
            if operator =='+':
                stack.append(stack.pop() + stack.pop())
            elif operator == '*':
                   stack.append(stack.pop() * stack.pop())
            elif operator == '-':
                x,y =stack.pop() ,stack.pop()
                stack.append(y-x)
            elif operator == '/':
                x,y =stack.pop() ,stack.pop()
                stack.append(int(y/x))
            else:
                stack.append(int(operator)) 
        return stack[0]                     