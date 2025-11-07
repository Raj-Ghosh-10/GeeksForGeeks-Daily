import bisect

class Solution:
    def maxProfit(self, jobs):
        jobs.sort(key=lambda x: x[1])
        n = len(jobs)
        
        dp = [0] * n
        dp[0] = jobs[0][2]

        end_times = [job[1] for job in jobs]
        
        for i in range(1, n):
            profit_including = jobs[i][2]

            idx = bisect.bisect_right(end_times, jobs[i][0]) - 1
            
            if idx != -1:
                profit_including += dp[idx]

            dp[i] = max(dp[i-1], profit_including)
        
        return dp[-1]