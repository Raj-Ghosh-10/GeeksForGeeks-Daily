class Solution:
    def getLongestPrefix(self, s):
        n = len(s)
        fail_table = [0] * n
        pattern_i = 0
        for i in range(1, n):
            while s[i] != s[pattern_i]:
                if pattern_i == 0:
                    break
                pattern_i = fail_table[pattern_i - 1]
            else:
                pattern_i += 1
                fail_table[i] = pattern_i
        if fail_table[-1] == 0:
            return -1
        shortest_suffix = fail_table[-1]
        while f := fail_table[shortest_suffix - 1]:
            shortest_suffix = f
        return n - shortest_suffix