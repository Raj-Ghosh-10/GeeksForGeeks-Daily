class Solution:
    def countPS(self, s):
        n = len(s)
        count = 0
        for center in range(2 * n - 1):
            left = center // 2
            right = left + center % 2  # Handles even-length centers
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= 2:  # Palindrome of length >=2
                    count += 1
                left -= 1
                right += 1
        return count