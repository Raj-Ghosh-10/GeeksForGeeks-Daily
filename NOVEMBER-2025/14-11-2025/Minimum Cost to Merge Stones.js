/**
 * @param {number[]} stones
 * @param {number} k
 * @return {number}
 */

class Solution {
    mergeStones(stones, k) {
        const n = stones.length;
        if ((n - 1) % (k - 1) !== 0) return -1;

        const pref = Array(n + 1).fill(0);
        for (let i = 0; i < n; i++) pref[i + 1] = pref[i] + stones[i];

        const INF = 1e15;
        const dp = Array.from({ length: n }, () =>
            Array.from({ length: n }, () =>
                Array(k + 1).fill(INF)
            )
        );

        for (let i = 0; i < n; i++) dp[i][i][1] = 0;

        for (let len = 2; len <= n; len++) {
            for (let i = 0; i + len - 1 < n; i++) {
                const j = i + len - 1;

                for (let t = 2; t <= k; t++) {
                    for (let mid = i; mid < j; mid += (k - 1)) {
                        if (dp[i][mid][1] === INF || dp[mid + 1][j][t - 1] === INF) continue;
                        dp[i][j][t] = Math.min(dp[i][j][t],
                            dp[i][mid][1] + dp[mid + 1][j][t - 1]
                        );
                    }
                }

                if (dp[i][j][k] < INF)
                    dp[i][j][1] = dp[i][j][k] + (pref[j + 1] - pref[i]);
            }
        }

        return dp[0][n - 1][1];
    }
}