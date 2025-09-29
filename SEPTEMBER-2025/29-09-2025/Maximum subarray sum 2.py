from collections import deque

class Solution:
    def maxSubarrSum(self, arr, a, b):
        n = len(arr)


        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + arr[i]
        
        dq = deque()
        res = float('-inf')
        
        for r in range(a, n+1):  
            # Maintain left index range: [r-b, r-a]
            # Add prefix[r-a] into deque (candidate for subarray starting point)
            while dq and prefix[dq[-1]] >= prefix[r-a]:
                dq.pop()
            dq.append(r-a)
            
            while dq and dq[0] < r-b:
                dq.popleft()
            
            res = max(res, prefix[r] - prefix[dq[0]])
        
        return res