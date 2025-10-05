// User function template for C++

class Solution {
    void dfs(vector<vector<int>> &mat, vector<vector<int>> &vis, int row, int col, string s, 
             vector<string> &res, map<pair<int,int>,string> &mp) {
        int n = mat.size();
        int m = mat[0].size();
        if (row == n-1 && col == m-1) {
            res.push_back(s);
            return;
        }
        vis[row][col] = 1;
        
        for (int i = -1; i <= 1 ; i++) {
            for (int j = -1 ; j <= 1; j++) {
                if (abs(i) == abs(j)) {
                    continue;
                }
                int nrow = row + i;
                int ncol = col + j;

                if (nrow >= 0 && nrow < n && ncol >= 0 && ncol < m && mat[nrow][ncol] == 1) {
                    if (!vis[nrow][ncol]) {
                        s += mp[{i,j}];
                        dfs(mat, vis, nrow, ncol, s, res, mp);
                        s.pop_back(); 
                    }
                }
            }
        }
        vis[row][col] = 0;
    }

  public:
    vector<string> findPath(vector<vector<int>> &mat) {
        int n = mat.size();
        int m = mat[0].size();
        
        vector<vector<int>> vis(n, vector<int>(m, 0));
        map<pair<int,int>,string> mp;
        mp[{0,-1}] = "L";
        mp[{1,0}] = "D";
        mp[{0,1}] = "R";
        mp[{-1,0}] = "U";
        
        if (mat[0][0] == 0) {
            return {};
        }
        string s = "";
        vector<string> res;
        dfs(mat, vis, 0, 0, s, res, mp);
        return res;
    }
};