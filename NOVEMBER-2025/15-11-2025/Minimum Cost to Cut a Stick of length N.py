class Solution:
    def minCutCost(self, n, cuts):
        m = len(cuts)
        arr = [0] + sorted(cuts) + [n]

        dp = [[0] * (m + 2) for _ in range(m + 2)]

        for length in range(2, m + 2):
            for i in range(m + 2 - length):
                j = i + length
                best = float('inf')

                for k in range(i + 1, j):
                    best = min(best, dp[i][k] + dp[k][j] + arr[j] - arr[i])

                dp[i][j] = 0 if best == float('inf') else best

        return dp[0][m + 1]