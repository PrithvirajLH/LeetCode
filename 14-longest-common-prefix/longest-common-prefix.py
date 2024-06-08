class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        if prefix in strs:
            return prefix
        else:
            if len(strs)==1:
                return strs[0]
            else:
                first  = strs[0]
                second = strs[1]
                for i in range(min(len(first),len(second))):
                    if first[0] != second[0]:
                        return("")
                        
                    elif first[i] == second[i]:
                        prefix = prefix + first[i]
                    else:
                        break
                
                if len(strs)>2:
                    for i in range(2,len(strs)):
                        curr = strs[i]
                        for j in range(min(len(prefix),len(curr))):
                            if prefix[j] == curr[j]:
                                if len(curr) > 1:
                                    continue
                                else:
                                    prefix = curr
                            else:
                                prefix = prefix[:j]
                                break

                return(prefix)
            


        
        
        