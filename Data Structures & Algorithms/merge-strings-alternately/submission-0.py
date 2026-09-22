class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = ""
        while i < min(len(word1), len(word2)) and j < min(len(word1), len(word2)):
            res += word1[i]
            i += 1
            res += word2[j]
            j += 1
        if len(word1) > len(word2):
            res += word1[i:]
        else:
            res += word2[j:]
        return res