class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {}

        def determineOrder(char):
            if char in orderMap:
                return orderMap[char]
            ind = 0
            for k in order:
                if k == char:
                    orderMap[char] = ind
                    return orderMap[char]
                ind += 1

        def isOrder(x, y): # x < y
            minLen = min(len(x), len(y))
            for i in range(minLen):
                if determineOrder(x[i]) < determineOrder(y[i]):
                    return True
                elif determineOrder(x[i]) > determineOrder(y[i]):
                    return False
                # else continue;
            return len(x) <= len(y)
        
        for i in range(1, len(words)):
            if not isOrder(words[i-1], words[i]):
                return False
        return True