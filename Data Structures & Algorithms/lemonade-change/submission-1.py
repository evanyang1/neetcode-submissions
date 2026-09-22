class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ht = {
            5: 0,
            10: 0,
            20: 0
        }
        for b in bills:
            if b == 5:
                ht[5] += 1
            elif b == 10:
                if ht[5] < 1:
                    return False
                ht[5] -= 1
                ht[10] += 1
            elif b == 20:
                if ht[5] >= 1 and ht[10] >= 1:
                    ht[5] -= 1
                    ht[10] -= 1
                elif ht[5] >= 3:
                    ht[5] -= 3
                else:
                    return False
                ht[20] += 1
        return True