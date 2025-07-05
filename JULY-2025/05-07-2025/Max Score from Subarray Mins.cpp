class Solution {
  public:
    int pairWithMaxSum(vector<int> &arr) {
        int maxSum = 0;
        
        for (int i = 0; i < arr.size() - 1; i++) {
            maxSum = max(maxSum, arr[i] + arr[i + 1]);
        }
        
        return maxSum;
    }
};
