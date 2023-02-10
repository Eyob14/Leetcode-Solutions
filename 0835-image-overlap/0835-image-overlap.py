class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        length = len(img1)
        Img_1_ones = [(x, y) for x in range(length) for y in range(length) if img1[x][y]]
        Imag_2_ones = [(x, y) for x in range(length) for y in range(length) if img2[x][y]]
        
        count = defaultdict(int)
        
        for Ax, Ay in Img_1_ones:
            for Bx, By in Imag_2_ones:
                vector = (Bx - Ax, By - Ay)
                count[vector] += 1
                
        return max(count.values()) if count.values() else 0
        