class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        size = len(s)
        word_size = len(words[0])
        window = len(words) * word_size
        answer = []
        hashMap = {}
        
        # Create a hashmap to count occurrences of each word
        for word in words:
            hashMap[word] = hashMap.get(word, 0) + 1
        
        # Slide over the string with the defined window size
        for i in range(size - window + 1):
            hashMap_temp = hashMap.copy()  # Copy the hashmap for current window
            for j in range(i, i + window, word_size):
                substr = s[j:j + word_size]
                if substr in hashMap_temp:
                    hashMap_temp[substr] -= 1
                    if hashMap_temp[substr] == 0:
                        del hashMap_temp[substr]  # Remove the word if count is zero
                else:
                    break
            if len(hashMap_temp) == 0:  # If all words are matched
                answer.append(i)  # Store the starting index
        return answer
        
        
        
        # res = []
        # n = len(words)
        # word_len = len(words[0])
        # word = n * word_len

        # for i in range(0, len(s)):
        #     if i+word > len(s):
        #         break
        #     sent = s[i:i + word]
        #     sent_list = []
        #     for k in range(0,len(sent), word_len):
        #         if k+word_len <= len(sent):
        #             sub = sent[k:k+word_len]
        #             sent_list.append(sub)
        #     flag = True
        #     for j in words:
        #         if j not in sent_list:
        #             flag = False
        #             break
        #         else:
        #             sent_list.remove(j)
        #     if flag:
        #         res.append(i)
        
        # return res
                
        