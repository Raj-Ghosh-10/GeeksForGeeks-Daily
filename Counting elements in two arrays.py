from bisect import bisect_right

class Solution:
    def countLessEq(self, a, b):
        b.sort()
        result = []
        for x in a:
            count = bisect_right(b, x)
            result.append(count)
        
        return result