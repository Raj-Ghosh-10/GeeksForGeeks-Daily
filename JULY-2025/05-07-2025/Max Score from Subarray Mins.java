import java.util.List;

class Solution {
    // Function to find pair with maximum sum
    public int pairWithMaxSum(List<Integer> arr) {
        int left = 0, right = 1;
        int max = Integer.MIN_VALUE;
        while(left<arr.size() && right<arr.size())
        {
            int sum = arr.get(left)+arr.get(right);
            if(sum>max)
            {
                max = Math.max(max,sum);
            }
            left++;
            right++;
        }
        return max;
    }
}