class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        max_len = 0
        dp[0] = {} 
        for i in range(1, len(nums)):
            dp[i] = {}
            for j in range(0, i):
                diff = nums[i]-nums[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff]+1
                else:
                    dp[i][diff] = 2
                max_len = max(max_len, dp[i][diff])
        return max_len
        