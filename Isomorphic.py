class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            iso = {}
            for index,c in enumerate(s):
                if len(iso) > 0:
                    if c in iso.keys() or t[index] in iso.values():
                        try:    
                            if iso[c] != t[index]:
                                return(False)
                        except: return(False)
                    else:   iso[c] = t[index]
                else:   iso[c] = t[index] 
        return(True)

print(Solution.isIsomorphic("","badc","baba"))