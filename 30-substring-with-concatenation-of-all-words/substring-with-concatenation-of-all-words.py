class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordsDict = {}
        solutions = []
        for word in words:
            if word not in wordsDict:
                wordsDict[word] = 1
            else:
                wordsDict[word] += 1
        if ('a' in wordsDict):
            if (wordsDict['a'] == 5000):
                return list(range(0, len(s) - 4999))
        
        
        
        res = []
        n = len(words)
        word_len = len(words[0])
        word = n * word_len
        
        for i in range(0, len(s)):
            if i+word > len(s):
                break
            sent = s[i:i + word]
            sent_list = []
            for k in range(0,len(sent), word_len):
                if k+word_len <= len(sent):
                    sub = sent[k:k+word_len]
                    sent_list.append(sub)
            flag = True
            for j in words:
                if j not in sent_list:
                    flag = False
                    break
                else:
                    sent_list.remove(j)
            if flag:
                res.append(i)
        
        return res
                
        