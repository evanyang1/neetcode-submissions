class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        res = 0
        for n in nums:
            res ^= n
        return res

