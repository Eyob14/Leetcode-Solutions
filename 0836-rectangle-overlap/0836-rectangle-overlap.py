class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        s1, t1, s2, t2 = rec2
        
        if (x1 == x2) or (y1 == y2) or (s1 == s2) or (t1 == t2):
            return False
        else:
            return not (x2 <= s1 or y2 <= t1 or x1 >= s2 or y1 >= t2)