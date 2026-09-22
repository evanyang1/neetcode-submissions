class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm={}
        l = len(nums)
        for n in nums:
            if n in hm:
                hm[n]+=1
            else:
                hm[n] = 1
        for k in hm:
            if hm[k] > l//2:
                print(k)
                return k