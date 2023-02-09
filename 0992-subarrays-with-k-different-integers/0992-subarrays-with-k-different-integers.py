class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def helper(nums, k):
            storage = {}
            subarrays = 0
            start, end = 0, 0
            while end < len(nums):
                if nums[end] in storage:
                    storage[nums[end]] += 1
                else:
                    storage[nums[end]] = 1
                    
                while len(storage) > k:
                    storage[nums[start]] -= 1
                    if storage[nums[start]] == 0:
                        del storage[nums[start]]    
                    start += 1
                    
                subarrays += end-start+1
                end += 1
                
            return subarrays
        
        return helper(nums, k) - helper(nums, k-1)
            
            
                
                
            
        