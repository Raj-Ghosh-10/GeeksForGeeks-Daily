/**
 * @param {number[]} arr
 * @return {number}
 */
class Solution {
    maxSumIS(arr) {
        const n = arr.length;
        const dp = [...arr];
        let ans = arr[0];
        for (let i = 1; i < n; i++) {
            for (let j = 0; j < i; j++) {
                if (arr[j] < arr[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + arr[i]);
                }
            }
            ans = Math.max(ans, dp[i]);
        }
        return ans;
    }
}