/**
 * @param {string} s
 * @return {number}
 */
class Solution {
    countSubs(s) {

        class State {
            constructor() {
                this.len = 0;
                this.link = -1;
                this.next = {};
            }
        }

        const n = s.length;
        const st = Array(2 * n).fill(0).map(() => new State());

        let size = 1;
        let last = 0;

        for (const ch of s) {
            let cur = size++;
            st[cur].len = st[last].len + 1;

            let p = last;

            while (p !== -1 && !(ch in st[p].next)) {
                st[p].next[ch] = cur;
                p = st[p].link;
            }

            if (p === -1) {
                st[cur].link = 0;
            } else {
                const q = st[p].next[ch];

                if (st[p].len + 1 === st[q].len) {
                    st[cur].link = q;
                } else {
                    const clone = size++;
                    st[clone].len = st[p].len + 1;
                    st[clone].link = st[q].link;
                    st[clone].next = { ...st[q].next };

                    while (p !== -1 && st[p].next[ch] === q) {
                        st[p].next[ch] = clone;
                        p = st[p].link;
                    }

                    st[q].link = clone;
                    st[cur].link = clone;
                }
            }

            last = cur;
        }

        let ans = 0;

        for (let i = 1; i < size; i++) {
            ans += st[i].len - st[st[i].link].len;
        }

        return ans;
    }
}