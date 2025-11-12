/**
 * @param {string} txt
 * @param {string} pat
 * @return {boolean}
 */
class Solution {
    wildCard(txt, pat) {
        const n = pat.length;
        const m = txt.length;
        let prev = new Array(m + 1).fill(false);
        let curr = new Array(m + 1).fill(false);
        prev[0] = true;
        for (let i = 1; i <= n; i++) {
            curr[0] = prev[0] && pat[i - 1] === '*';
            for (let j = 1; j <= m; j++) {
                const p = pat[i - 1];
                const t = txt[j - 1];
                if (p === t || p === '?') {
                    curr[j] = prev[j - 1];
                } else if (p === '*') {
                    curr[j] = prev[j] || curr[j - 1];
                } else {
                    curr[j] = false;
                }
            }
            prev = curr.slice();
            curr.fill(false);
        }
        return prev[m];
    }
}