class Solution:
    
    def addBinary(self, a: str, b: str) -> str:
        def convert(x:str) -> int:
            l = len(x)-1
            x = list(map(int,x))
            sum = 0
            for i in x:
                sum = sum + (i*(pow(2,l)))
                l-=1
            return sum
        a = convert(a)
        b= convert(b)
        a = bin(a + b)
        return a[2:]
        
    
        


            
        