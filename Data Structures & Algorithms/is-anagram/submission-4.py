class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for x in s:
            seen[x] = seen.get(x, 0) + 1
        for y in t:
            if y not in seen:
                return False
            seen[y] -= 1
            if seen[y] < 0:
                return False
        return True