class Solution:
    def powerfulInteger(self, intervals, k):
        events = []
        for start, end in intervals:
            events.extend([(start, -1), (end, 1)])
        events.sort()
        cnt, ans = 0, -1
        for t, typ in events:
            if typ == -1:
                cnt += 1 
            else:
                if cnt >= k:
                    ans = max(ans, t)
                cnt -= 1
        return ans