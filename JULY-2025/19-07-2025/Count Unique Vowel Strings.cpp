class Solution {
  public:
    int f(int n){
        if(n == 0 || n == 1){
          return 1;
        }
        return n * f(n - 1);
    }
    
    int vowelCount(string& s) {
        unordered_map<int,int>mp;
        
        int cnt = 1;
        string v = "aeiou";
        
        for(int i = 0; i < s.size();i++){
            if(v.find(s[i]) != string::npos){
                mp[s[i]]++;
            }
        }
        
        if(mp.size() == 0){
            return 0;
        }
        
        for(auto&it:mp){
            cnt *= it.second;
        }
        
        
        return f(mp.size()) * cnt;
    }
};