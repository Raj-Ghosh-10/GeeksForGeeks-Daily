class Solution {
    public int hIndex(int[] citations) {
        // code here
        int n = citations.length;
        int high = Integer.MIN_VALUE;
        int low = 0;
        
        for(int num : citations) {
            if(num > high) high = num;
        }
        
        while(low <= high) {
            int mid = (low + high) / 2;
            if(isPossible(citations,mid,n)) {
                low = mid + 1;
            }else{
                high = mid - 1;
            }
        }
        
        return high;
    }
    
    public boolean isPossible(int[] citations, int val, int n) {
        int cnt = 0;
        
        for(int num : citations) {
            if(num >= val) cnt += 1;
        }
        
        return cnt >= val;
    }
}