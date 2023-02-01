# Description
___
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

```
Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

# Solution

```Python
    def TwoSum(self, nums, target):
        num_dict = {}
        for i in range(len(nums)):
            num_dict[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_dict and i != num_dict[diff]:
                return [i, num_dict[diff]]
            return []
```