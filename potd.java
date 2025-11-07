class Solution {
    public int maxProfit(int[][] jobs) {
        Arrays.sort(jobs, (a, b) -> Integer.compare(a[1], b[1]));
        int n = jobs.length;
        int[] dp = new int[n];
        dp[0] = jobs[0][2];
        int[] endTimes = new int[n];
        for (int i = 0; i < n; i++) endTimes[i] = jobs[i][1];
        for (int i = 1; i < n; i++) {
            int includeProfit = jobs[i][2];
            int idx = binarySearch(endTimes, jobs[i][0], i - 1);
            if (idx != -1) includeProfit += dp[idx];
            dp[i] = Math.max(dp[i - 1], includeProfit);
        }
        return dp[n - 1];
    }
    private int binarySearch(int[] endTimes, int startTime, int high) {
        int low = 0, ans = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
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