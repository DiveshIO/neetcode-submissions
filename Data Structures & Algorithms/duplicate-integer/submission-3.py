class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = set()
        for x in nums:
            if x in found:
                return True
            found.add(x)
        return False