class Solution:
    def vowelCount(self, s):
        #code here
        dic={}
        for i in s:
            if i in 'aeiou': # Finding Vowel Character
                if i in dic:
                    dic[i]+=1 # Adding Occurrences of Vowel Character
                else:
                    dic[i]=1
            
        values= list(dic.values())
        keys= list(dic.keys())
 
        factorial=1
        for i in range(1,len(keys)+1):  # Factorial of distinct character present in S
            factorial*=i
        
        for i in range(len(values)): # Multiplying with number of Occurrences of each character
            if values[i]>1:
                factorial*=values[i]
                
        if dic: 
            return factorial
        return 0  # String with no vowel