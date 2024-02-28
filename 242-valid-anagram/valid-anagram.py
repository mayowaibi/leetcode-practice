class Solution:
    # From scratch
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = {}
        for c in s:
            if c not in sMap:
                sMap[c] = 0
            sMap[c] += 1

        tMap = {}
        for c in t:
            if c not in tMap:
                tMap[c] = 0
            tMap[c] += 1

        for key in sMap.keys():
            if (key not in tMap) or (sMap[key] != tMap[key]):
                return False
        return True

    # Using in-build method
    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)