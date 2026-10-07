class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_number = {}
        for x in range(len(nums)):
            diff = target - nums[x]
            if diff in seen_number:
                return [seen_number[diff], x]
            seen_number[nums[x]] = x
        return []