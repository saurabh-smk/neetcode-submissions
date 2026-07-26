class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1, s2 = 0,0
        merged_string = ''

        while s1<len(word1) and s2<len(word2):
            merged_string += word1[s1]
            s1+=1

            merged_string += word2[s2]
            s2+=1
        
        if s1<len(word1):
            merged_string += word1[s1:]
        if s2<len(word2):
            merged_string += word2[s2:]

        return merged_string

        