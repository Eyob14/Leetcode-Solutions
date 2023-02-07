class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_, max_ = min(nums), max(nums)
        size = abs(min_)+abs(max_)+1
        
        array = [0]*size
        
        for num in nums:
            array[num-min_] += 1
        
        for i in range(size-1, -1, -1):
            if k-array[i] > 0:
                k -= array[i]
            else:
                return i+min_