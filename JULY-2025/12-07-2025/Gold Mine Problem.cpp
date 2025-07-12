class Solution {
  public:
  int f(int i,int j,vector<vector<int>>&mat,vector<vector<int>>&dp){
      if(i<0 || j<0 || i>=mat.size() || j>=mat[0].size()) return 0;
      if(dp[i][j]!=-1) return dp[i][j];
      int op1=f(i+1,j+1,mat,dp);
      int op2=f(i,j+1,mat,dp);
      int op3=f(i-1,j+1,mat,dp);
      
      return dp[i][j]=max(op1,max(op2,op3))+mat[i][j];
  }
    int maxGold(vector<vector<int>>& mat) {
        int maxi=0;
        int n=mat.size();
        int m=mat[0].size();
        vector<vector<int>>dp(n+1,vector<int>(m+1,-1));
        for(int i=0;i<mat.size();i++){
            
            maxi=max(maxi,f(i,0,mat,dp));
        }
        return maxi;
        
    }
};