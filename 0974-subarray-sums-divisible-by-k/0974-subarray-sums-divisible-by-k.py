class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_fre = defaultdict(int)
        remainder_fre[0] = 1
        ans, cur_sum = 0, 0

        for num in nums:
            cur_sum += num
            ans += remainder_fre[cur_sum%k]
            remainder_fre[cur_sum%k] += 1
            
        return ans
