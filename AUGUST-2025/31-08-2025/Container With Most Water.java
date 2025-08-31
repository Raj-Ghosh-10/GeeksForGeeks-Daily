class Solution {
    public int maxWater(int arr[]) {
        // Code Here
        int n = arr.length;
        int left = 0 , right = n-1;
        
        int res = 0;
        while(left < right)
        {
            int water = Math.min(arr[left],arr[right]) * (right - left);
            res = Math.max(res,water);
            
            if(arr[left] < arr[right])left++;
            else right--;
        }
        return res;
    }
}

 