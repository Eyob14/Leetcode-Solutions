class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_freq = max(count.values())
        
        answer = float("inf")
        left, right = 0, 0
        cur_count = Counter()
        
        while right < len(nums):
            cur_e = nums[right]
            cur_count[cur_e] += 1
            right += 1
            while cur_count[cur_e] == max_freq:
                answer = min(answer, right-left)
                cur_count[nums[left]] -= 1
                left += 1
                
        return answer
        
        
        