class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [i for i in range(len(nums) + 1)]
        s = set(arr)
        for n in nums:
            if n in s:
                s.remove(n)
        return list(s)[0]
