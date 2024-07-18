class Solution:
    def reverseWords(self, s: str) -> str:

        res = s.split()
        return " ".join(res[::-1])


        # stack = []
        # temp = ''
        # res = ""

        # for i in s:
        #     if i != " ":
        #         temp += i
        #     else:
        #         if temp:
        #             stack.append(temp)
        #             temp = ''
        # stack.append(temp)

        # while stack:
        #     res += stack.pop()
        #     res += " "

        # return res.strip()
        