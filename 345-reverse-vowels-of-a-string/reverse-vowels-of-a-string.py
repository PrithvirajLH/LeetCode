class Solution:
    def reverseVowels(self, s: str) -> str:
        res = ''
        vowels = []
        for i in range(len(s)):
            if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
                vowels.append(s[i])

        for i in range(len(s)):
            if s[i] in ['a','e','i','o','u', 'A','E','I','O','U']:
                res += vowels.pop()
                i += 1
            else:
                res += s[i]
        return res