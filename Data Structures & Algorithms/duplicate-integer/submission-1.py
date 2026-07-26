class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        nums = sorted(nums)

        pointer_a = 0

        while (pointer_a < len(nums)-1):
            if nums[pointer_a] == nums[pointer_a + 1]:
                return True
            
            pointer_a = pointer_a + 1


        return False