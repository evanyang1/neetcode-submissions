class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        sMap,tMap = {},{}
        for ch in s:
            if ch in sMap:
                sMap[ch]+=1
            else:
                sMap[ch]=1
        for ch in t:
            if ch in tMap:
                tMap[ch]+=1
            else:
                tMap[ch]=1
        return sMap == tMap