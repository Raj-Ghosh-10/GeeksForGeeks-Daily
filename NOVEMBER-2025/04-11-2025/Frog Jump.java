class Solution {
    int minCost(int[] height) {
        int n = height.length;
        if (n == 1){ 
            return 0;
        }
        int prev = 0;
        int prev2 = 0;
        for (int i = 1; i < n; i++) {
            int jump1 = prev + Math.abs(height[i] - height[i - 1]);
            int jump2 = Integer.MAX_VALUE;
            if (i > 1) {
                jump2 = prev2 + Math.abs(height[i] - height[i - 2]);
            }
            int curr = Math.min(jump1, jump2);
            prev2 = prev;
            prev = curr;
        }
        return prev;
    }
}