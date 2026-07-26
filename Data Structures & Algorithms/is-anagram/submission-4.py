from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # if len(s)!=len(t):
        #     return False
        
        # _s = set(s)

        # for item in _s:
        #     if item in t:
        #         continue

        #     else:
        #         return False

        # return True
