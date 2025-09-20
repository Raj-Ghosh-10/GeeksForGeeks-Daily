class Solution {
  public:
    int longestSubarray(vector<int>& arr){
        int n=arr.size();
        vector<int>nextg(n,n);
        vector<int>prevg(n,-1);
        stack<int>st;
        for(int i=n-1;i>=0;i--){
            while(!st.empty() && arr[st.top()]<=arr[i]){
                st.pop();
            }
            if(!st.empty()){
                nextg[i]=st.top();
            }
            st.push(i);
        }
        while(!st.empty()){
            st.pop();
        }
        for(int i=0;i<n;i++){
            while(!st.empty() && arr[st.top()]<=arr[i]){
                st.pop();
            }
            if(!st.empty()){
                prevg[i]=st.top();
            }
            st.push(i);
        }
        int ans=0;
        for(int i=0;i<n;i++){
            int a=nextg[i]-prevg[i]-1;
            if(a>=arr[i]){
                ans=max(ans,a);
            }
        }
        return ans;
    }
};