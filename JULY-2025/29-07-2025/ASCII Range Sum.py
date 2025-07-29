class Solution:
    def asciirange(self, s):
        # code here
        position = {}
        for i in range(len(s)):
            if s[i] not in position:
                position[s[i]] = [i,-1]
            else:
                position[s[i]][1] = i
        
        
        dp = [0] * len(s)
        
        for i in range(len(s)):
            if i > 0:
                dp[i] = dp[i-1] + ord(s[i])
            else:
                dp[i] = ord(s[i])
        
        res =[]
        
        for i,j in position.values():
            if j == -1:
                continue
            
            if dp[j-1] - dp[i] > 0:
                res.append(dp[j-1] - dp[i])
        
        return res