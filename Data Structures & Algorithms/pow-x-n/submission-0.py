class Solution:
    def myPow(self, x: float, n: int) -> float:
        def myPowHelper(x,n):
            if n == 0:
                return 1.0
            if n < 0:
                return 1/myPowHelper(x,-1*n)
            if n == 1:
                return x
            if n == 2:
                return x*x
            if n % 2 == 0:
                return myPowHelper(x, n//2)*myPowHelper(x, n//2)
            else:
                return myPowHelper(x, n//2)*myPowHelper(x, n//2)*x

        return myPowHelper(x,n)