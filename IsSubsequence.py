class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s is None or t is None:
            return False
        sIdx = 0
        for letter in t:
            if sIdx == len(s):
                break
            if s[sIdx] == letter:
                sIdx += 1
        return sIdx == len(s)