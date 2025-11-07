/**
 * @param {number[][]} jobs
 * @returns {number}
 */

class Solution {
    maxProfit(jobs) {
        jobs.sort((a, b) => a[1] - b[1]);
        const n = jobs.length;
        const dp = Array(n).fill(0);
        dp[0] = jobs[0][2];
        const endTimes = jobs.map(job => job[1]);
        for (let i = 1; i < n; i++) {
            let includeProfit = jobs[i][2];
            let idx = this.binarySearch(endTimes, jobs[i][0], i - 1);
            if (idx !== -1) includeProfit += dp[idx];
            dp[i] = Math.max(dp[i - 1], includeProfit);
        }
        return dp[n - 1];
    }
    binarySearch(endTimes, startTime, high) {
        let low = 0, ans = -1;
        while (low <= high) {
            const mid = Math.floor((low + high) / 2);
            if (endTimes[mid] <= startTime) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
}