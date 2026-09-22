class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = Counter(nums)
        res = []
        print(d)
        for x in d:
            print(x)
            if d[x] > n // 3:
                res.append(x)
        return res