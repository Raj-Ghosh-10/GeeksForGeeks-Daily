class Solution {
    public int minSuperSeq(string s1, string s2) {
        int n = s1.Length;
        int m = s2.Length;
        int[,] dp = new int[n + 1, m + 1];

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (s1[i - 1] == s2[j - 1])
                    dp[i, j] = 1 + dp[i - 1, j - 1];
                else
                    dp[i, j] = Math.Max(dp[i - 1, j], dp[i, j - 1]);
            }
        }

        int lcsLength = dp[n, m];
        return n + m - lcsLength;
    }
}