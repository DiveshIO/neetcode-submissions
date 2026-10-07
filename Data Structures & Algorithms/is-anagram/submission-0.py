class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = list(s)
        for p in t:
            if p in x:
                x.remove(p)
            else:
                return False
        return len(x) == 0
        