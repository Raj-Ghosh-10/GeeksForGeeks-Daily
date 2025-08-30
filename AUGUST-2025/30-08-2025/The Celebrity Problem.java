class Solution {
    public int celebrity(int mat[][]) {
        // Two Pointor Approach
        int n = mat.length;
        int l = 0, r = n-1;
        
        // Step 1: Eliminate non-celebrities
        while(l < r)
        {
            if(mat[l][r] == 1) 
                l++; // l knows r → l can't be celebrity
            else 
                r--; // l doesn't know r → r can't be celebrity
        }
        
        // Step 2: Verify candidate
        int candidate = l;
        for (int i = 0; i < n; i++) 
        {
            if (i == candidate) continue;
            // check if candidate knows someone OR someone doesn't know candidate
            if ((mat[candidate][i] == 1) || (mat[i][candidate] == 0)) 
            {
                return -1; 
            }
        }

        return candidate;
    }
}