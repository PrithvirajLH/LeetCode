class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s:
            seen = s[0]
        else:
            return 0
        
        longest = 0

        for i in range(1,len(s)):
            if s[i] not in seen:
                seen += s[i]
            else:
                start = 0
                longest = max(longest, len(seen))
                seen += s[i]
                while seen[start] != s[i]:
                    start += 1
                seen = seen[start + 1 :]
        longest = max(longest, len(seen))
        return longest

        