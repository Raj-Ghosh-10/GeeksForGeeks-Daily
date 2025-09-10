class Solution:
    def largestSwap(self, s):
        #code here
        swap = [0] * len(s)
        greater = len(s) - 1
        swap[-1] = greater
        for i in range(len(s)-2, -1, -1):
            if int(s[i]) > int(s[greater]):
                greater = i
                
            swap[i] = greater
        
        res = list(s)
        for i in range(len(s)):
            if int(s[i]) == int(s[swap[i]]):
                continue
            
            res[i], res[swap[i]] = res[swap[i]], res[i]
            break
        
        return ''.join(res)