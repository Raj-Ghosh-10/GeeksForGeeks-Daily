/**
 * @param {number[]} arr
 * @returns {number}
 */

class Solution {
    maxProfit(arr) {
        const n = arr.length;
        if (n === 0) return 0;
        let hold = -arr[0];
        let sold = 0;
        let rest = 0;
        for (let i = 1; i < n; i++) {
            const prevHold = hold;
            const prevSold = sold;
            const prevRest = rest;
            hold = Math.max(prevHold, prevRest - arr[i]);
            sold = prevHold + arr[i];
            rest = Math.max(prevRest, prevSold);
        }
        return Math.max(sold, rest);
    }
}