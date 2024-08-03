class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        var1 = Counter(word1)
        var2 = Counter(word2)
        arr1 = []
        arr2 = []
        key1 = []
        key2 = []
        for k, v in var1.items():
            arr1.append(v)
            key1.append(k)
        for k, v in var2.items():
            arr2.append(v)
            key2.append(k)
        arr1.sort()
        arr2.sort()
        key1.sort()
        key2.sort()
        return arr1 == arr2 and key1 == key2
        