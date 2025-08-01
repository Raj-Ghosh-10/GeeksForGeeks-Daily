class Solution {
    private:
    bool isVowel(char ch){
        if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'){
            return true;
            
        }
        else{
            return false;
        }
    }
  public:
    int countBalanced(vector<string>& arr) {
        // code here
        int balance=0;
        int total=0;
        unordered_map<int, int> mp;
        mp[balance]=1;
        for (auto i: arr){
            for(char ch: i){
                if(isVowel(ch)){
                    balance++;
                }
                else{
                    balance--;
                }
            }
            total+= mp[balance];
            mp[balance]++;
        }
        return total;
    }
};