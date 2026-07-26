class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for idx, s in enumerate(strs[0]):
            # print('top', idx, s)
            for st in strs:
                # print('in', st, st[idx])
                if idx >= len(st):
                    return st
                if s != st[idx]:
                    # print('condn', st, idx)
                    return st[:idx]
        return strs[0]
        

        