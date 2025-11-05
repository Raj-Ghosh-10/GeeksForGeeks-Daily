class Solution:
    def isPerfect(self, x):
        r = int(x**0.5)
        return r*r == x

    def minSquares(self, n):
        if self.isPerfect(n):
            return 1
        
        for i in range(1, int(n**0.5) + 1):
            if self.isPerfect(n - i*i):
                return 2
        
        temp = n
        while temp % 4 == 0:
            temp //= 4
        
        if temp % 8 == 7:
            return 4
            
        return 3