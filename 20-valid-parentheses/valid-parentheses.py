class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        top = -1
        for i in s:
            if i in "({[":
                stack.append(i)
                top += 1
            else:
                if stack:
                    if i == ")" and stack[top] == "(":
                        stack.pop()
                        top -= 1
                    elif i == "}" and stack[top] == "{":
                        stack.pop()
                        top -= 1
                    elif i == "]" and stack[top] == "[":
                        stack.pop()
                        top -= 1
                    else:
                        break
                else:
                    return False
        return len(stack) == 0


        