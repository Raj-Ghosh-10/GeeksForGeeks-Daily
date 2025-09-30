class Solution:
    def binstr(self, n):
        return [format(i, '0{}b'.format(n)) for i in range(1 << n)]

 