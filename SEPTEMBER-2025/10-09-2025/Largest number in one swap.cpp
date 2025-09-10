class Solution {
  public:
    string largestSwap(string &s) {
        // code here
        int n=s.length();
        
        
        // suppose at i=0 its 7 
        // and on i=3,5 both there is 8 
        // which one will be swapped?
        // i=3
        
        // so we have to find first largest value next to i
        // supppose i=0 7 
        // i=3 8
        // i=4 9
        
        // then i=4 will bes used for swapping
        
        for (int i = 0; i < n - 1; i++) {
            int maxDigit = s[i];
            int maxIdx = -1;
            
            // Find the largest digit after index i
            for (int j = n - 1; j > i; j--) {
                if (s[j] > maxDigit) {
                    maxDigit = s[j];
                    maxIdx = j;
                }
            }
            
            // If a larger digit exists after i, swap and return result
            if (maxIdx != -1) {
                swap(s[i], s[maxIdx]);
                return s;
            }
        }
        
        // If no swap was made, return the original string
        return s;
    }
};