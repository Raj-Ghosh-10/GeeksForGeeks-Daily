class Solution {
    subsetXOR(n) {
        let totalXOR = 0;
        for (let i = 1; i <= n; i++) totalXOR ^= i;
        if (totalXOR === n) {
            return Array.from({length: n}, (_, i) => i + 1);
        } else {
            const x = totalXOR ^ n;
            let ans = [];
            for (let i = 1; i <= n; i++) {
                if (i !== x) ans.push(i);
            }
            return ans;
        }
    }
}