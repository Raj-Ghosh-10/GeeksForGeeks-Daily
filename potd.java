class Solution {
    boolean isPerfect(int x) {
        int r = (int)Math.sqrt(x);
        return r * r == x;
    }
    public int minSquares(int n) {
        if (isPerfect(n)) {
            return 1;
        }
        for (int i = 1; i * i <= n; i++) {
            if (isPerfect(n - i * i)){
                return 2;
            }
        }
        int temp = n;
        while (temp % 4 == 0) {
            temp /= 4;
        }
        if (temp % 8 == 7) {
            return 4;
        }
        return 3;
    }
}