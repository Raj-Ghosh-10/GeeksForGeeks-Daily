class Solution:
    def maxSumIS(self, arr):
        n = len(arr)
        dp = arr[:]
        ans = arr[0]
        for i in range(1, n):
            for j in range(i):
                if arr[j] < arr[i]:
                    dp[i] = max(dp[i], dp[j] + arr[i])
            ans = max(ans, dp[i])
        return ans