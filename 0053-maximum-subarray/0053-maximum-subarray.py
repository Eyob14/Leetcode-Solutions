class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        @cache
        def helper(i, pick, lookup={}):
            if (i,pick) in lookup:
                return lookup[(i,pick)]
            if i >= len(nums):
                return 0 if pick else -inf
            picked = nums[i]+helper(i+1, True)
            passed = 0 
            if not(pick):
                passed = helper(i+1, False)
            return max(picked, passed)
        
        return helper(0, False)