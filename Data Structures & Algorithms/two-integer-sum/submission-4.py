class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for n in range(len(nums)):
            remainder = target-nums[n]
            if remainder in seen:
                return sorted([n,seen[remainder]])
            seen[nums[n]] = n