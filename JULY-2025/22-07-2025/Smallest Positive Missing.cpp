
class Solution {
  public:
    // Function to find the smallest positive number missing from the array.
    int missingNumber(vector<int> &arr) {
        // Your code here
        int maxi=*max_element(arr.begin(),arr.end());
        if(maxi<=0){
            return 1;
        }
        unordered_set<int>st(arr.begin(),arr.end());
        for(int i=1;i<=maxi;i++){
            if(st.find(i)==st.end()){
                return i;
            }
        }
        return maxi+1;
    }
};