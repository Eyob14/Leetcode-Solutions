class Solution:
    def checkValidString(self, s: str) -> bool:
        """
            The trick for this problem is how can we use the wild card either as an open or
            closing parenthesis. to determine that we can maintain two variables that always give
            us the minimum and maximum open parenthesis we have.
            
            minimum parenthesis means we are assuming * to be closing parenthesis
            maximum parenthesis means we are assuming * to be opening parenthesis
            
            if maxmimum no of parenthesis we have is negetive at any point we can return False
            if minimum parenthesis < 0 update to be 0
            
            at the end check if maxmimum no of parenthesis == 0
            
            Time complexiy - O(N)
            Space Complexiyt - O(1)
        """
        
        star_is_open_parenthesis = 0
        star_is_close_parenthesis = 0
            
        for letter in s:
            if letter == "(":
                star_is_open_parenthesis += 1
                star_is_close_parenthesis += 1 
            elif letter == ")":
                star_is_open_parenthesis -= 1
                star_is_close_parenthesis -= 1   
            else:
                star_is_open_parenthesis += 1
                star_is_close_parenthesis -= 1   
            if star_is_open_parenthesis < 0:
                return False
            if star_is_close_parenthesis < 0:
                star_is_close_parenthesis = 0
            
        return star_is_close_parenthesis == 0