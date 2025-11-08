class Solution {
    public int numberOfPath(int[][] mat, int k) {
        int n = mat.length;
        int m = mat[0].length;
        int[][][] dp = new int[n][m][k + 1];
        if (mat[0][0] <= k)
            dp[0][0][mat[0][0]] = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int sum = 0; sum <= k; sum++) {
                    if (i == 0 && j == 0) continue;
                    if (sum < mat[i][j]) continue;
                    int remaining = sum - mat[i][j];
                    int ways = 0;
                    if (i > 0) ways += dp[i - 1][j][remaining];
                    if (j > 0) ways += dp[i][j - 1][remaining];
                    dp[i][j][sum] = ways;
                }
            }
        }
        return dp[n - 1][m - 1][k];
    }
}