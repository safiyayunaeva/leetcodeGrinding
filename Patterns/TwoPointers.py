"""
Two sum on sorted array
"""


def twoSum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
            currentSum = nums[left] + nums[right]
            if currentSum == target:
                return [nums[left], nums[right]]
            elif currentSum < target:
                left += 1
            else:
                right -= 1
    return []

# usage
nums = [1,2,7,11,15,25]
target = 9
print(twoSum(nums, target)) # Output [2, 7]