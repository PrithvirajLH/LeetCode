class Solution(object):
    def isValid(self, s):
        stack = []
        top=-1
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
                top += 1
            elif top > -1:
                if stack[top] == '(' and char == ')' :
                    stack.pop(top)
                    top -= 1
                elif stack[top] == '{' and char == '}':
                    stack.pop(top)
                    top -= 1
                elif stack[top] == '[' and char == ']':
                    stack.pop(top)
                    top -= 1
                else:
                    return False
            else:
                return False
        if top == -1:
            return True
        else:
            return False

        
        