class Solution {
    public ArrayList<Integer> farMin(int[] arr) {
        int n = arr.length;
        ArrayList<Integer> ans = new ArrayList<>(Collections.nCopies(n, -1));

        // Step 1: Build suffix minimum array
        int[] suffMin = new int[n];
        suffMin[n - 1] = arr[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffMin[i] = Math.min(arr[i], suffMin[i + 1]);
        }

        // Step 2: For each index, binary search in suffix
        for (int i = 0; i < n; i++) {
            int l = i + 1, r = n - 1, res = -1;
            while (l <= r) {
                int mid = (l + r) / 2;
                if (suffMin[mid] < arr[i]) {
                    res = mid;   // mid is a valid candidate
                    l = mid + 1; // try to go farther right
                } else {
                    r = mid - 1;
                }
            }
            ans.set(i, res);
        }

        return ans;
    }
}