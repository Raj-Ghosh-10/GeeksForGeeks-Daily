class Solution {
    public List<int> SubsetXOR(int n) {
        List<int> ans = new List<int>();
        int totalXOR = 0;
        for (int i = 1; i <= n; i++) totalXOR ^= i;
        if (totalXOR == n) {
            for (int i = 1; i <= n; i++) ans.Add(i);
        } else {
            int x = totalXOR ^ n;
            for (int i = 1; i <= n; i++) {
                if (i != x) ans.Add(i);
            }
        }
        return ans;
    }
}