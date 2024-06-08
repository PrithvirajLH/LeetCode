class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        len_prefix = len(prefix)

        for i in strs[1:]:
            while prefix != i[0:len_prefix]:
                len_prefix -= 1
                if len_prefix == 0:
                    return ""
                prefix = prefix[0:len_prefix]
        return prefix
        