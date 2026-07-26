class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = 2 * n * [0]

        for i, num in enumerate(nums):
            ans[i] = num
            ans[i+n] = num
        
        return ans

        