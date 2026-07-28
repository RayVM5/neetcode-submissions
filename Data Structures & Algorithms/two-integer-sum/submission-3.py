class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in range(len(nums)):
            left = list(nums[:n]+nums[n+1:])
            remainder = (target-nums[n])
            if remainder in left:
                j_index = left.index(remainder)
                return sorted([j_index+1,n])