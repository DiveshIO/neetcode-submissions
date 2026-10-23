class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_num = {}
        for idx, elm in enumerate(nums):
            tar = target - elm
            if tar in seen_num:
                return [seen_num[tar], idx]
            seen_num[elm] = idx
        return [-1,-1]