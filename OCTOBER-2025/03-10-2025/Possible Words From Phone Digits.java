

//User function Template for Java

class Solution {
    // Function to find list of all words possible by pressing given numbers.
    static ArrayList<String> possibleWords(int a[], int N) {
        // Map for keypad mappings
        Map<Integer, List<Character>> keypad = new HashMap<>();
        
        keypad.put(2, Arrays.asList('a', 'b', 'c'));
        keypad.put(3, Arrays.asList('d', 'e', 'f'));
        keypad.put(4, Arrays.asList('g', 'h', 'i'));
        keypad.put(5, Arrays.asList('j', 'k', 'l'));
        keypad.put(6, Arrays.asList('m', 'n', 'o'));
        keypad.put(7, Arrays.asList('p', 'q', 'r', 's'));
        keypad.put(8, Arrays.asList('t', 'u', 'v'));
        keypad.put(9, Arrays.asList('w', 'x', 'y', 'z'));

        // List to store all possible words
        ArrayList<String> result = new ArrayList<>();
        
        // Recursive function to generate words
        getSS(a, 0, N, result, keypad, "");
        
        return result;
    }

    // Static recursive helper function to generate the combinations
    public static void getSS(int a[], int index, int N, ArrayList<String> result, 
                             Map<Integer, List<Character>> keypad, String curr) {
        // Base case: if we've processed all digits, add the current word to the result
        if (index == N) {
            if (!curr.isEmpty())
                result.add(curr);
            return;
        }
        
        // Handle special case for '1' and '0'
        if (a[index] == 1) {
            // Skip digit '1' (since it has no corresponding letters)
            getSS(a, index + 1, N, result, keypad, curr);
        } else if (a[index] == 0) {
            // Handle digit '0' (usually mapped to space or nothing)
            getSS(a, index + 1, N, result, keypad, curr + ' ');
        } else {
            // Handle regular digits (2-9)
            int number = a[index];
            List<Character> valuesForNum = keypad.get(number);
            
            // Loop over all characters mapped to the current digit
            for (char value : valuesForNum) {
                // Recursively build the word
                getSS(a, index + 1, N, result, keypad, curr + value);
            }
        }
    }
}