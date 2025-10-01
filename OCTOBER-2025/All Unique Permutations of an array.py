from itertools import permutations
from typing import List
class Solution:
    def uniquePerms(self, arr):

        all_perms_iterator = permutations(arr)
        

        unique_perms_set = set(all_perms_iterator)
        

        result = sorted([list(p) for p in unique_perms_set])
        
        return result