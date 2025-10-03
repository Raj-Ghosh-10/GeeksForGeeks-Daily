class Solution:
    def dfs(self,ind,temp,arr,keypad,res):
        if len(temp)==len(arr):
            res.append("".join(temp))
            return 
        
        chars = keypad[arr[ind]]
        
        for s in chars:
            temp.append(s)
            self.dfs(ind+1,temp,arr,keypad,res)
            temp.pop()
            
    def possibleWords(self, arr):
        arr = [i for i in arr if i not in {0,1}]
        
        keypad = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        
        res = []

        self.dfs(0,[],arr,keypad,res)
        
        return res