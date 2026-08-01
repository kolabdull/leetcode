
nums = [2, 7, 11, 15]
target = 9

class Solution:
    def twoSum(self, nums, target):
        notebook = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in notebook:
                return [notebook[diff], i]
            notebook[n] = i

