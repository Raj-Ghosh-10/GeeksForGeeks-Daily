public class Solution {
    public int minCost(int[] height) {
        int n = height.Length;
        if (n == 1) return 0;
        int prev = 0;
        int prev2 = 0;
        for (int i = 1; i < n; i++) {
            int jump1 = prev + Math.Abs(height[i] - height[i - 1]);
            int jump2 = int.MaxValue;
            if (i > 1) {
                jump2 = prev2 + Math.Abs(height[i] - height[i - 2]);
            }
            int curr = Math.Min(jump1, jump2);
            prev2 = prev;
            prev = curr;
        }
        return prev;
    }
}