class Solution {
  public:
    int powerfulInteger(vector<vector<int>>& intervals, int k) {
        if (intervals.empty() || k == 0) return -1;
        vector<pair<int, int>> events;
        for (auto& interval : intervals) {
            events.push_back({interval[0], 1});
            events.push_back({interval[1] + 1, -1});
        }
        sort(events.begin(), events.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            if (a.first == b.first) {
                return a.second < b.second;
            }
            return a.first < b.first;
        });
        
        int maxPowerful = -1; 
        int activeIntervals = 0; 
        int lastPos = INT_MIN; 
        for (auto& event : events) {
            int pos = event.first;
            int type = event.second;
            if (activeIntervals >= k && lastPos != INT_MIN) {
                maxPowerful = max(maxPowerful, pos - 1);
            }
            activeIntervals += type;
            lastPos = pos;
        }
        
        return maxPowerful;
    }
};