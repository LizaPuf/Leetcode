


'''Given an integer x, return true if x is a 
palindrome
, and false otherwise.'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
           return False
        x_str = str(x)
        if x_str == x_str[::-1]:
            return True
        return False



'''Roman to Integer'''
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        correction_dict = {'IV': -2, 'IX': -2,
                        'XL': -20, 'XC': -20,
                        'CD': -200, 'CM': -200}

        for i in s:
            total += roman_dict[i]
        for key in correction_dict:
            if key in s:
                total += correction_dict[key]
        return total






