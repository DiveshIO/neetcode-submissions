class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicts = {}
        for x in nums:
            if dicts.get(x,0 ) != 0:
                return True
            else:
                dicts[x] = 1
        return False
         