class Solution {
public:
    int maxProfit(vector<vector<int>> &jobs) {
        sort(jobs.begin(), jobs.end(), [](auto &a, auto &b) {
            return a[1] < b[1];
        });
        int n = jobs.size();
        vector<int> dp(n);
        dp[0] = jobs[0][2];
        vector<int> endTimes(n);
        for (int i = 0; i < n; i++) endTimes[i] = jobs[i][1];
        for (int i = 1; i < n; i++) {
            int includeProfit = jobs[i][2];
            int l = 0, r = i - 1, idx = -1;
            while (l <= r) {
                int mid = (l + r) / 2;
                if (endTimes[mid] <= jobs[i][0]) {
                    idx = mid;
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
            if (idx != -1) includeProfit += dp[idx];
            dp[i] = max(dp[i - 1], includeProfit);
        }
        return dp[n - 1];
    }
};