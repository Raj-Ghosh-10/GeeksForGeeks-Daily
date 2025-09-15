class Solution {
  public:
    int startStation(vector<int> &gas, vector<int> &cost) {
        int n=gas.size();
        int totalgas=0;
        int currgas=0;
        int idx=0;
        for(int i=0;i<n;i++){
            totalgas+=gas[i]-cost[i];
            currgas+=gas[i]-cost[i];
            if(currgas<0){
                idx=i+1;
                currgas=0;
            }
        }
        if(totalgas>=0){
            return idx;
        }
        return -1;
    }
};