class Solution {
    public bool wildCard(string txt, string pat) {
        int n = pat.Length;
        int m = txt.Length;
        bool[] prev = new bool[m + 1];
        bool[] curr = new bool[m + 1];
        prev[0] = true;
        for (int i = 1; i <= n; i++) {
            curr[0] = prev[0] && pat[i - 1] == '*';
            for (int j = 1; j <= m; j++) {
                char p = pat[i - 1];
                char t = txt[j - 1];
                if (p == t || p == '?')
                    curr[j] = prev[j - 1];
                else if (p == '*')
                    curr[j] = prev[j] || curr[j - 1];
                else
                    curr[j] = false;
            }
            Array.Copy(curr, prev, m + 1);
            Array.Clear(curr, 0, m + 1);
        }
        return prev[m];
    }
}