class Solution {
  public:
    int substrCount(string &s, int k) {
        // code here
        int count = 0;
        int n = s.size();
        unordered_map<int,int>m;
        for(int i=0;i<k;i++){
            m[s[i]]++;
        }
        if(m.size()==k-1){
            count++;
        }
        int left = 0,right = k;
        while(right<n){
            m[s[right]]++;
            m[s[left]]--;
            if(m[s[left]]==0){
                m.erase(s[left]);
            }
            if(m.size()==k-1){
                count++;
            }
            left++;
            right++;
        }
        return count;
    }
};