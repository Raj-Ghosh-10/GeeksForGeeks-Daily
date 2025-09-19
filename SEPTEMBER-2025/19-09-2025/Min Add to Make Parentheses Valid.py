class Solution:
    def minParentheses(self, s):
        # code here
        list1 = []
        count = 0
        for char in s:
            if char == '(': #adding to stack
                list1.append(char)
            elif char == ')':
                if len(list1) == 0: #checking if stack is empty
                    count +=1
                elif len(list1) != 0: #if stack not empty,
                #pop top element as it has matching parenthesis
                    list1.pop()
        return len(list1) + count