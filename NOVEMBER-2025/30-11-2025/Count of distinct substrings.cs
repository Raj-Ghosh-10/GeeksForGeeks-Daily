class Solution
{
    class State
    {
        public int len, link;
        public int[] next = new int[26];

        public State()
        {
            len = 0;
            link = -1;
            for (int i = 0; i < 26; i++) next[i] = -1;
        }
    }

    public int countSubs(string s)
    {
        int n = s.Length;
        State[] st = new State[2 * n];
        for (int i = 0; i < 2 * n; i++) st[i] = new State();

        int size = 1;
        int last = 0;

        foreach (char ch in s)
        {
            int c = ch - 'a';
            int cur = size++;
            st[cur].len = st[last].len + 1;

            int p = last;

            while (p != -1 && st[p].next[c] == -1)
            {
                st[p].next[c] = cur;
                p = st[p].link;
            }

            if (p == -1)
            {
                st[cur].link = 0;
            }
            else
            {
                int q = st[p].next[c];
                if (st[p].len + 1 == st[q].len)
                {
                    st[cur].link = q;
                }
                else
                {
                    int clone = size++;
                    st[clone].len = st[p].len + 1;
                    st[clone].link = st[q].link;
                    Array.Copy(st[q].next, st[clone].next, 26);

                    while (p != -1 && st[p].next[c] == q)
                    {
                        st[p].next[c] = clone;
                        p = st[p].link;
                    }

                    st[q].link = clone;
                    st[cur].link = clone;
                }
            }

            last = cur;
        }

        long ans = 0;

        for (int i = 1; i < size; i++)
        {
            ans += st[i].len - st[st[i].link].len;
        }

        return (int)ans;
    }
}