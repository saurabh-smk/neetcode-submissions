class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pointer_a = 0

        while pointer_a<len(nums):
            pointer_b = pointer_a + 1
            while (pointer_b > pointer_a and pointer_b < len(nums)):
                if nums[pointer_a] + nums[pointer_b] == target:
                    return [pointer_a, pointer_b]
                
                pointer_b += 1

            pointer_a += 1
