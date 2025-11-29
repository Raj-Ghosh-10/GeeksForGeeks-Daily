class Solution {
    countSetBits(N) {
        let count = 0;
        while (N > 0) {
            let x = Math.floor(Math.log2(N)); // position of MSB
            count += x * (1 << (x - 1));
            count += N - (1 << x) + 1;
            N -= (1 << x);
        }
        return count;
    }
}