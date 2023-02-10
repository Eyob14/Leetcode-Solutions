class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        elements = []
        idx_1 = idx_2 = 0

        while idx_1 < len(nums1) and idx_2 < len(nums2):
            if nums1[idx_1] < nums2[idx_2]:
                elements.append(nums1[idx_1])
                idx_1 += 1
            else:
                elements.append(nums2[idx_2])
                idx_2 += 1
        while idx_1 < len(nums1):
            elements.append(nums1[idx_1])
            idx_1 += 1
        while idx_2 < len(nums2):
            elements.append(nums2[idx_2])
            idx_2 += 1

        
        index = len(elements)//2
        if len(elements) % 2 == 0:
            return (elements[index] + elements[index-1])/2
        else:
            return elements[index]
        