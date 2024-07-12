class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        i = ""
        for j in s:
            if j == "(":
                stack.append(i)
                i = ""
            elif j == ")":
                i = i[::-1]
                i = stack.pop() + i
            else:
                i += j
        return i

        # for i in s:
        #     if i == ")":
        #         rev = ""
        #         while stack and stack[-1] != "(":
        #             rev += stack.pop()
        #         if stack:
        #             stack.pop()
        #         for j in rev:
        #             stack.append(j)
        #     else:
        #         stack.append(i)
        
        # return "".join(stack)


        