class Solution {
  public:
    vector<int> asciirange(string& s) {
        // code here
        vector<int>ans;
        unordered_map<int,int>mpp, res;
        vector<int>prefixSum(s.size(), 0);
        for(int i = 0;i<s.size();i++){
            int ch = s[i] - 'a';
            if(mpp.find(ch)!=mpp.end()){
                if(res.find(ch)!=res.end())
                 res[ch] = fmax(res[ch], prefixSum[i-1] - prefixSum[mpp[ch]]);
                else 
                    res[ch] = prefixSum[i-1] - prefixSum[mpp[ch]];
            }else{
                mpp[ch] = i;
            }
            int temp = s[i];
            if(i)prefixSum[i] = prefixSum[i-1] + s[i];
            else prefixSum[i] = s[i];
            
        }
        for(auto it : res) if(it.second)ans.push_back(it.second);
        return ans;
    }
};