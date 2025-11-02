class Solution {
  public:
    int maxEdgesToAdd(int V, vector<vector<int>>& edges) {
        // code here
        int maxEdges = (V*(V-1)/2) ;
        int noOfEdges = edges.size();
        return maxEdges-noOfEdges ;
    }
};