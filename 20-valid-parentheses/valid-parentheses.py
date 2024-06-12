class Solution:
    def isValid(self, s: str) -> bool:
        top = -1
        storage = []
        entry = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in entry:
                if storage and storage[top]==entry[i]:
                    storage.pop(top)
                    top -= 1
                else:
                    return False
            elif i in '({[':
                storage.append(i)
                top += 1
        return not storage


        