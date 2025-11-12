class Solution:
    def wildCard(self, txt, pat):
        n, m = len(pat), len(txt)

        prev = [False] * (m + 1)
        curr = [False] * (m + 1)

        prev[0] = True

        for i in range(1, n + 1):
            curr[0] = prev[0] and pat[i - 1] == '*'

            for j in range(1, m + 1):
                p, t = pat[i - 1], txt[j - 1]

                if p == t or p == '?':
                    curr[j] = prev[j - 1]
                elif p == '*':
                    curr[j] = prev[j] or curr[j - 1]
                else:
                    curr[j] = False

            prev, curr = curr, [False] * (m + 1)

        return prev[m]