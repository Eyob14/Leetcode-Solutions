class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        num = 0
        index = len(s)-1
        
        while index >= 0 and index-1 > -1:
            if s[index-1]+s[index] not in roman:
                num += roman[s[index]]
                index -= 1
            else:
                num += roman[s[index-1]+s[index]]
                index -= 2
        if index == 0:
            num += roman[s[index]]
            
        return num