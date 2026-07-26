class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
                
        # return []

        difference = {}
        for idx, num in enumerate(nums):
            diff = target - num

            if diff in difference:
                return [difference[diff], idx]
            
            difference[num] = idx
        return []
        