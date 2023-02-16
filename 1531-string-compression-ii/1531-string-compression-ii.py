class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp(idx, curr, curr_count, remains):
            
            if idx == len(s):
                return 0
            
            
            del_char_dis = inf
            if remains > 0:
                del_char_dis = dp(idx+1, curr, curr_count, remains - 1)
            
            curr_letter = s[idx]
            
            chr_cost = inf
            if curr_letter == curr:
                add = 0

                if curr_count == 1 or len(str(curr_count + 1)) > len(str(curr_count)):
                    add = 1
                
                chr_cost = add + dp(idx+1, curr_letter, curr_count + 1, remains)
            else:
                chr_cost = 1 + dp(idx+1, curr_letter, 1, remains)
            
            return min(chr_cost, del_char_dis)
                
            
        res = dp(0, "", 0, k)
        return res