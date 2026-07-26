from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Solution 1
        # return Counter(s) == Counter(t) => fastest
        
        # Solution 2

        if len(s) != len(t):
            return False

        t_counter_hash = Counter(t)

        for item in s:
            if item in t_counter_hash:
                t_counter_hash[item] = t_counter_hash[item] - 1

        if any([freq>0 for freq in t_counter_hash.values()]):
            return False
        else:
            return True
