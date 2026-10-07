class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for x in s:
            seen[x] = seen.get(x, 0) + 1
        for y in t:
            if y not in seen:
                return False
            seen[y] = seen.get(y, 0) - 1
        for x in seen:
            if seen[x] != 0:
                return False
        
        return True