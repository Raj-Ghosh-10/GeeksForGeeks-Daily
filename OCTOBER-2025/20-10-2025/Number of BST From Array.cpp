class Solution {
  public:
    vector<int> countBSTs(vector<int>& arr) {
        // Code here
        // sort(arr.begin(), arr.end());
        unordered_map<int, int>catalan;
        //in the constraints its is given that the array size if only uppt ot 6 suze
        catalan[0]=1;
        catalan[1]=1;
        catalan[2]=2;
        catalan[3]=5;
        catalan[4]=14;
        catalan[5]=42;
        catalan[6]=132;
        catalan[7]=429;
        vector<int> ans(arr.size(), 1);;
        vector<pair<int, int>> vec;
        for(int i=0; i<arr.size(); i++){
            vec.push_back(make_pair(arr[i], i));
        }
        sort(vec.begin(), vec.end());
        for(int i=0; i<vec.size(); i++){
            int start= i;
            int end= vec.size()-i-1;
            int index= vec[i].second;
            ans[index]= catalan[start] * catalan[end];
            
        }
        return ans;
        
    }
};