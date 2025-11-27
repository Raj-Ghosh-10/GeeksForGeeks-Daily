
class Solution
{
    public int SubsetXorSum(int[] arr)
    {
        int n = arr.Length;
        int ans = 0;

        for (int bit = 0; bit <= 10; bit++)
        {
            int countSet = 0;
            foreach (int num in arr)
            {
                if ((num & (1 << bit)) != 0)
                    countSet++;
            }

            if (countSet > 0)
            {
                ans += (1 << bit) * (1 << (n - 1));
            }
        }

        return ans;
    }
}