class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given 2 String
        s <-
        t <-
        True if two strings are anagrams
            - string are anagram if they contain the same character
        
        we can do sorted == sorted
        Space: O(n)
        TIme: O(n lgn)
        have a hashmap
        Space: O(n)
        Time: O(n) + O(n)
        """
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