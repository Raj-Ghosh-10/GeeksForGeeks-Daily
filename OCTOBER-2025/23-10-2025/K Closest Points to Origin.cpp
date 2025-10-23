class Solution {
  public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // code here
        priority_queue<pair<int,pair<int,int>>> pq;
        vector<vector<int>> res;
        int n=points.size();
        for(int i=0;i<n && i<k;i++){
           int value = points[i][0]*points[i][0]+points[i][1]*points[i][1];
           pq.push({value,{points[i][0],points[i][1]}});
        }
        for(int i=k;i<n;i++){
             int value = points[i][0]*points[i][0]+points[i][1]*points[i][1];
                 pq.push({value,{points[i][0],points[i][1]}});
                 pq.pop();
        }
         n=pq.size();
        for(int i=0;i<n;i++){
            res.push_back({pq.top().second.first,pq.top().second.second});
            pq.pop();
        }
        reverse(res.begin(),res.end());
        return res;
    }
};