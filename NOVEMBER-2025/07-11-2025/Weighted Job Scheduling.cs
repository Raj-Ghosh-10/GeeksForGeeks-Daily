class Solution {
    public int maxProfit(int[,] jobsArray) {
        int n = jobsArray.GetLength(0);
        List<int[]> jobs = new List<int[]>();
        for (int i = 0; i < n; i++) {
            jobs.Add(new int[] { jobsArray[i, 0], jobsArray[i, 1], jobsArray[i, 2] });
        }
        jobs.Sort((a, b) => a[1].CompareTo(b[1]));
        int[] dp = new int[n];
        dp[0] = jobs[0][2];
        int[] endTimes = new int[n];
        for (int i = 0; i < n; i++) endTimes[i] = jobs[i][1];
        for (int i = 1; i < n; i++) {
            int includeProfit = jobs[i][2];
            int idx = BinarySearch(endTimes, jobs[i][0], i - 1);
            if (idx != -1) includeProfit += dp[idx];
            dp[i] = Math.Max(dp[i - 1], includeProfit);
        }
        return dp[n - 1];
    }
    private int BinarySearch(int[] endTimes, int startTime, int high) {
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