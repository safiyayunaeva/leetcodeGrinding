from typing import List


def twosum(nums: List[int], target: int) -> List[int]:
    """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.
    """
    cache = {}
    for index, value in enumerate(nums):
        if value in cache:
            return  [cache[value], index]
        cache[target - value] = index
    return [0, 0]

def runningSum(nums: List[int]) -> List[int]:
    """
    https://leetcode.com/problems/running-sum-of-1d-array/
    :param nums:
    :return:
    """
    result = [nums[0]]
    for i in range(1, len(nums)):
        result.append(result[i - 1] + nums[i])

    return result