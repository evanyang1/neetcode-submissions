class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def getLengthShortest():
            res = 200
            for s in strs:
                res = max(res, len(s))
            return res

        def isArrayElementsEqual(arr):
            if len(arr) <= 1:
                return True
            for i in range(1, len(arr)):
                if arr[i] != arr[0]:
                    return False
            return True

        def processIndex(i):
            arr = []
            for s in strs:
                if i >= len(s):
                    return False
                arr.append(s[i])
            return isArrayElementsEqual(arr)

                
        longestPrefix = ""
        lenShortest = getLengthShortest()
        for i in range(lenShortest):
            if processIndex(i):
                longestPrefix += strs[0][i]
            else:
                return longestPrefix

        