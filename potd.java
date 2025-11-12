class Solution {
    public boolean wildCard(String txt, String pat) {
        int n = pat.length();
        int m = txt.length();
        boolean[] prev = new boolean[m + 1];
        boolean[] curr = new boolean[m + 1];
        prev[0] = true;
        for (int i = 1; i <= n; i++) {
            curr[0] = prev[0] && pat.charAt(i - 1) == '*';
            for (int j = 1; j <= m; j++) {
                char p = pat.charAt(i - 1);
                char t = txt.charAt(j - 1);
                if (p == t || p == '?') {
                    curr[j] = prev[j - 1];
                } else if (p == '*') {
                    curr[j] = prev[j] || curr[j - 1];
                } else {
                    curr[j] = false;
                }
            }
            prev = curr.clone();
            curr = new boolean[m + 1];
        }
        return prev[m];
    }
}