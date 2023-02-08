class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maximum = max(nums)
        unique = list(set(nums))
        unique.sort()
        if len(unique) > 2:
            return unique[-3]
        return maximum
        