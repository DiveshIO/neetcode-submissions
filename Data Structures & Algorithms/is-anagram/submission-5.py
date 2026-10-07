class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_words = {}
        if len(s) != len(t):
            return False
        for x in s:
            seen_words[x] = seen_words.get(x, 0) + 1
        for y in t:
            if seen_words.get(y, 0) <= 0:
                return False
            seen_words[y] -= 1
        return True