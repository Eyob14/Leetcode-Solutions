class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        answer = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    answer = max(answer, nums[j]-nums[i])
        return answer