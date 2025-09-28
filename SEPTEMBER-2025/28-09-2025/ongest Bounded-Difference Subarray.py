class Solution:
    def longestSubarray(self, arr, x):
        #code here
        from collections import deque
        n = len(arr)
        max_deque = deque()
        min_deque = deque()
        left = 0
        best_len = 0
        best_start = 0

        for right in range(n):
            # Maintain decreasing order in max_deque
            while max_deque and arr[right] > arr[max_deque[-1]]:
                max_deque.pop()
            max_deque.append(right)

            # Maintain increasing order in min_deque
            while min_deque and arr[right] < arr[min_deque[-1]]:
                min_deque.pop()
            min_deque.append(right)

            # Shrink window if condition violated
            while arr[max_deque[0]] - arr[min_deque[0]] > x:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            # Update best window
            if right - left + 1 > best_len:
                best_len = right - left + 1
                best_start = left

        return arr[best_start: best_start + best_len]