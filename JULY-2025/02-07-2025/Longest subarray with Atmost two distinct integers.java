class Solution {
    public static int totalFruits(Integer[] arr) {
        int basket1 = 0;
        int basket2 = 0;
        int count1 = 0;
        int count2 = 0;
        int maxLen = Integer.MIN_VALUE;
        
        for(int right = 0; right < arr.length; right++) {
            
            if(count1 == 0) {
                basket1 = arr[right];
                count1++;
            } else if(basket1 == arr[right]) {
                count1++;
            } else if(count2 == 0) {
                basket2 = arr[right];
                count2++;
            } else if(basket2 == arr[right]) {
                count2++;
            } else {
                basket1 = basket2;
                count1 = count2;
                basket2 = arr[right];
                count2 = 1;
            }
            
            maxLen = Math.max(maxLen, count1 + count2);
        }
        
        return maxLen;
    }
}