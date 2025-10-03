
class Solution {
  public:
  void possibleWordsRec(vector<int> &arr, int index, string &prefix, 
                      vector<string> &padMap, vector<string> &res) {
    if (index == arr.size()) {
        res.push_back(prefix);
        return;
    }
    int digit = arr[index];
    if (digit < 2 || digit > 9) {
        possibleWordsRec(arr, index + 1, prefix, padMap, res);
        return;
    }

    for (char ch : padMap[digit]) {
        prefix.push_back(ch);
        possibleWordsRec(arr, index + 1, prefix, padMap, res);
        prefix.pop_back();
    }
}

    vector<string> possibleWords(vector<int> &arr) {
        // code here
        vector<string> res;
    vector<string> padMap = {"", "", "abc", "def", "ghi", "jkl",
                                     "mno", "pqrs", "tuv", "wxyz"};
    string prefix = "";

    possibleWordsRec(arr, 0, prefix, padMap, res);
    return res;
    }
};