class Solution(object):
    def TwoSum(self, nums, target):
        num_dict = {}
        for i in range(len(nums)):
            num_dict[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_dict and i != num_dict[diff]:
                return [i, num_dict[diff]]
            return []






