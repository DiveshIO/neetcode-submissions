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
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for x in count:
            if x != 0:
                return False
        return True