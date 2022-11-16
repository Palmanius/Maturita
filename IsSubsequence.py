class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        found = 0
        if len(s) == 0:
            return True
        else:
            for c in t:
                if c == s[found]:
                    found += 1
                if found == len(s):
                    return True
        return False


print(Solution.isSubsequence("","","ahbgdc"))