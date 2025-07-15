class Solution:
    def divby13(self, s):
        # code here 
        mod=0
        for digit in s:
            mod=(mod*10 + int(digit))%13
        return mod==0