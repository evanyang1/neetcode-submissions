class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        g = {i: [] for i in range(1, n+1)}
        for t in trust:
            src, dest = t
            g[src].append(dest)
        possibleTJarr = []
        for j in range(1, n + 1):
            if len(g[j]) == 0:
                possibleTJarr.append(j)
        if len(possibleTJarr) != 1:
            return -1
        possibleTJ =  possibleTJarr[0]

        def searchArr(arr, x):
            for xx in arr:
                if xx == x:
                    return True
            return False

        for i in range(1, n+1):
            if i == possibleTJ:
                continue
            if not searchArr(g[i], possibleTJ):
                return -1
        return possibleTJ