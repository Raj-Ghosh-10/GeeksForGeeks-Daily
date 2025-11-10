class Solution {
    public int maxProfit(int[] arr) {
        int n = arr.Length;
        if (n == 0) return 0;
        int hold = -arr[0];
        int sold = 0;
        int rest = 0;
        for (int i = 1; i < n; i++) {
            int prevHold = hold;
            int prevSold = sold;
            int prevRest = rest;
            hold = Math.Max(prevHold, prevRest - arr[i]);
            sold = prevHold + arr[i];
            rest = Math.Max(prevRest, prevSold);
        }
        return Math.Max(sold, rest);
    }
}