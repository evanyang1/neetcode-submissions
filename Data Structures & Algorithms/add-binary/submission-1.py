class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]
        for i in range(max(len(a), len(b))):
            digitA = a[i] if i < len(a) else 0
            digitB = b[i] if i < len(b) else 0
            c = int(digitA) + int(digitB) + carry
            carry = c // 2
            res = str(c % 2) + res
        if carry:
            res = "1" + res
        return res

