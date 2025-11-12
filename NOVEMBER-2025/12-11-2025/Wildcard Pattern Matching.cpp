class Solution {
public:
    bool wildCard(string &txt, string &pat) {
        int n = pat.size(), m = txt.size();
        vector<bool> prev(m + 1, false), curr(m + 1, false);
        prev[0] = true;
        for (int i = 1; i <= n; i++) {
            curr[0] = prev[0] && (pat[i - 1] == '*');
            for (int j = 1; j <= m; j++) {
                if (pat[i - 1] == txt[j - 1] || pat[i - 1] == '?'){
                    curr[j] = prev[j - 1];
                }else if (pat[i - 1] == '*'){
                    curr[j] = prev[j] || curr[j - 1];
                }else{
                    curr[j] = false;
                }
            }
            prev = curr;
            fill(curr.begin(), curr.end(), false);
        }
        return prev[m];
    }
};