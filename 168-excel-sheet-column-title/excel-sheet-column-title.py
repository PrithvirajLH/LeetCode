class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber:
            columnNumber, remainder = divmod(columnNumber-1, 26)
            ans = ans + chr(65 + remainder)
        return ans[::-1]