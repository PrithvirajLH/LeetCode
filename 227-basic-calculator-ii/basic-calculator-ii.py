class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(op, val):
            if op == "+": stack.append(val)
            elif op == "-": stack.append(-val)
            elif op == "*": stack.append(stack.pop()*val)
            elif op == "/": stack.append(int(stack.pop()/val))
        i = 0
        num = 0
        stack = []
        sign = "+"

        while i < len(s):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i] in "+-*/":
                evaluate(sign, num)
                num = 0
                sign = s[i]
            i += 1
        evaluate(sign, num)
        return sum(stack)
        