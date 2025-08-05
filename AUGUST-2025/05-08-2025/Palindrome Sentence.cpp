class Solution {
  public:
    bool isPalinSent(string &s) {
        // code here
        string newS = "";
        for(auto it : s)
        {
            char c = tolower(it);
            int asciiVal = int(c);
            if((asciiVal >= 97 && asciiVal <= 122) || (asciiVal >= 48 && asciiVal <= 57))
            {
                newS += c;
            }
        }
        int i = 0, j = newS.length() - 1;
        while(i <= j)
        {
            if(newS[i] != newS[j])
            {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
};