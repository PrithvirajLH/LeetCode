class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        s = re.findall("\w", s)
        s = ''.join(s).lower()
        s = re.sub("\_", "", s)
        last = len(s)
        if len(s)> 1:
            while s[first] == s[last-1]:
                if first<last:
                    first += 1
                    last -= 1
                else:
                    return True
        else:
            return True
        return False
