/**
 * @param {number} n
 * @returns {number}
 */

class Solution {
    isPerfect(x) {
        const r = Math.floor(Math.sqrt(x));
        return r * r === x;
    }
    minSquares(n) {
        if (this.isPerfect(n)){
          return 1;  
        } 
        for (let i = 1; i * i <= n; i++) {
            if (this.isPerfect(n - i * i)){
              return 2;  
            } 
        }
        let temp = n;
        while (temp % 4 === 0) {
            temp /= 4;
        }
        if (temp % 8 === 7){
           return 4; 
        } 
        return 3;
    }
}