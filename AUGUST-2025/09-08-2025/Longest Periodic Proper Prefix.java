class Solution {
    int getLongestPrefix(String s) {
        int n = s.length();
        if(n<=1) return -1;
        int[] lps = new int[n];
        
        // Build LPS array (KMP prefix function)
        int len = 0; 
        for (int i = 1; i < n; ) {
            if (s.charAt(i) == s.charAt(len)) {
                lps[i++] = ++len;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i++] = 0;
                }
            }
        }
        
        // Check longest periodic proper prefix
       // Traverse borders (proper prefix == suffix lengths)
        int j = lps[n - 1];
        if (j == 0) return -1;

        int minBorder = Integer.MAX_VALUE;
        while (j > 0) {
            minBorder = Math.min(minBorder, j);
            j = lps[j - 1];
        }

        if (minBorder == Integer.MAX_VALUE) return -1;
        int ans = n - minBorder;
        return ans > 0 ? ans : -1;
    }
}