/**
 * @param {string} s1
 * @param {string} s2
 * @returns {number}
 */
class Solution {
    minSuperSeq(s1, s2) {
        const n = s1.length;
        const m = s2.length;
        const dp = Array.from({ length: n + 1 }, () => Array(m + 1).fill(0));

        // Compute LCS
        for (let i = 1; i <= n; i++) {
            for (let j = 1; j <= m; j++) {
                if (s1[i - 1] === s2[j - 1]) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        const lcsLength = dp[n][m];
        return n + m - lcsLength;
    }
}