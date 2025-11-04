/**
 * @param {number[]} height
 * @return {number}
 */

class Solution {
    minCost(height) {
        const n = height.length;
        if (n === 1) return 0;
        let prev = 0;
        let prev2 = 0;
        for (let i = 1; i < n; i++) {
            let jump1 = prev + Math.abs(height[i] - height[i - 1]);
            let jump2 = Infinity;
            if (i > 1) {
                jump2 = prev2 + Math.abs(height[i] - height[i - 2]);
            }
            let curr = Math.min(jump1, jump2);
            prev2 = prev;
            prev = curr;
        }
        return prev;
    }
}