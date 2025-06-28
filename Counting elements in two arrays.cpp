class Solution {
  public:
    vector<int> countLessEq(vector<int>& a, vector<int>& b) {
        // code here
        sort(b.begin(),b.end());
        
        vector<int> ans;
        
        for(int i=0;i<a.size();i++){
            int p = lower_bound(b.begin(),b.end(),a[i]) - b.begin();
            
            while(p < b.size() && b[p] <= a[i]){
                p++;
            }
            
            ans.push_back(p);
        }
        
        return ans;
    }
};