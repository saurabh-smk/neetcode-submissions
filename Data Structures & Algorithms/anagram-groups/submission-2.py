class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            item = "".join(sorted(s))
            if item not in group.keys():
                group[item]=[s]
            else:
                group[item].append(s)

        return list(group.values())