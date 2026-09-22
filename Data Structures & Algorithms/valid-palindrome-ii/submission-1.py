class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(st, left, right):
            while left < right:
                if st[left] != st[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Try deleting left character or right character
                return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
        
        return True