class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        left = [0]+nums[:]
        right = nums[:]+[0]
        
        for i in range(1, length):
            left[i] += left[i-1]
        
        for i in range(length-2, -1, -1):
            right[i] += right[i+1]

        left = left[:-1]
        right = right[1:]
        for i in range(length):
            if left[i] == right[i]:
                return i
        
        return -1