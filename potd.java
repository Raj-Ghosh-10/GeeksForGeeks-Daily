class Solution {
    public int chocolatePickup(int[][] mat) {
        int n = mat.length;
        if (n == 0 || mat[0][0] == -1 || mat[n - 1][n - 1] == -1) {
            return 0;
        }
        int NEG = -1_000_000_000;
        int[][] dp = new int[n][n];
        for (int[] row : dp) {
            Arrays.fill(row, NEG);
        }
        dp[0][0] = mat[0][0];
        for (int k = 1; k <= (n - 1) * 2; k++) {
            int[][] newDp = new int[n][n];
            for (int[] row : newDp) {
                Arrays.fill(row, NEG);
            }
            int iMin = Math.max(0, k - (n - 1));
            int iMax = Math.min(n - 1, k);
            for (int i1 = iMin; i1 <= iMax; i1++) {
                int j1 = k - i1;
                if (j1 < 0 || j1 >= n || mat[i1][j1] == -1) continue;
                for (int i2 = iMin; i2 <= iMax; i2++) {
                    int j2 = k - i2;
                    if (j2 < 0 || j2 >= n || mat[i2][j2] == -1) continue;
                    int best = dp[i1][i2];
                    if (i1 > 0) best = Math.max(best, dp[i1 - 1][i2]);
                    if (i2 > 0) best = Math.max(best, dp[i1][i2 - 1]);
                    if (i1 > 0 && i2 > 0) best = Math.max(best, dp[i1 - 1][i2 - 1]);
                    if (best <= NEG / 2) continue;
                    int val = mat[i1][j1];
                    if (i1 != i2 || j1 != j2) {
                        val += mat[i2][j2];
                    }
                    newDp[i1][i2] = Math.max(newDp[i1][i2], best + val);
                }
            }
            dp = newDp;
        }
        return Math.max(0, dp[n - 1][n - 1]);
    }
}