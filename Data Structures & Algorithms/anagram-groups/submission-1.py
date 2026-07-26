class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for st in strs:
            sortst = sorted(st)
            res[tuple(sortst)].append(st)
        return list(res.values())
        

            
            

        