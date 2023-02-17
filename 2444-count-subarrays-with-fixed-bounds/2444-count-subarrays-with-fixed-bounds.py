class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        left, right = 0, 0
        lastMin = lastMax = None
        
        while right < len(nums):
            if nums[right] > maxK or nums[right] < minK:
                right += 1
                left = right
                lastMin = lastMax = None
                continue

            if nums[right] == minK:
                lastMin = right 
            if nums[right] == maxK:
                lastMax = right
                
            if lastMin != None and lastMax != None:
                ans += min(lastMin, lastMax) - left + 1  
            right += 1

        return ans
        