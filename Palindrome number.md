# Description
___
Given an integer x, return true if x is a 
palindrome
, and false otherwise.



```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

# Solution

```Python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
           return False
        x_str = str(x)
        if x_str == x_str[::-1]:
            return True
        return False
```