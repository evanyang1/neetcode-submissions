class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newDigit = 0
        pos = len(digits) - 1
        borrow = 0
        while pos >= 0:
            if digits[pos] != 9:
                digits[pos] += 1
                return digits
            else:
                digits[pos] = 0
                if pos == 0:
                    return [1] + digits
                else:
                    pos -= 1
        return digits
            
