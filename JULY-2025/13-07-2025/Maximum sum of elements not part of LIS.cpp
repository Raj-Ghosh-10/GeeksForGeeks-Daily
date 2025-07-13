
// User function Template for C++

class Solution {
  public:
    int maxSumLis(int arr[], int n) {
        vector<int>lis,ins(n);
        
        long long totalSum=0;
        for(int i=0 ; i<n ; i++){
            totalSum+=arr[i];
            auto lb=lower_bound(lis.begin(),lis.end(),arr[i]);
            if(lb==lis.end()){
                lis.push_back(arr[i]);
                ins[i]=lis.size()-1;
            }
            else{
                *lb=arr[i];
                ins[i]=lb-lis.begin();
            }
        }
        
        int lisSum=0 , ind=lis.size()-1;
        for(int i=n-1 ; i>=0 ; i--){
            if(ins[i]==ind){
                lisSum+=arr[i];
                ind--;
            }
        }
        return totalSum-lisSum;
    }
};