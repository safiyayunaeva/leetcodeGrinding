from typing import List

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


def is_balanced(string_to_check):
    open = "("
    closed = ")"
    count = 0
    for s in string_to_check:
        if s is open:
            count += 1
        if s is closed:
            count -= 1
    if count == 0:
        return True
    else:
        return False



def matching_parenteces(exp):
    pairs = {"{": "}", "[": "]", "(": ")"}
    open = ["{", "[", "("]
    closed = ["}", "]", ")"]

    stack = []
    for s in exp:
        if s in open:
            stack.append(pairs[s])
        if s in closed:
            if not stack:
                return False
            if stack.pop() is not s:
                return False
    if stack:
        return False
    else:
        return True


def twosum(nums: List[int], target: int) -> List[int]:
    """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.
    """
    cache = {}
    for index, value in enumerate(nums):
        if value in cache:
            return [cache[value], index]
        cache[target - value] = index
    return [0, 0]

def test_twosum():
    a = "((a+b)*c)+(b*a)"
    assert is_balanced(a) is True
 #   print(is_balanced(a))
 #   print(matching_parenteces(a))

from typing import List


def compress(chars: List[str]) -> int:
    # two pointers

    i = 0
    res = 0

    while i < len(chars):
        group_len = 1
        while i < len(chars) - 1 and chars[i] == chars[i + 1]:
            group_len += 1
            i += 1
        chars[res] = chars[i]
        res += 1
        if group_len > 1:
            for val in str(group_len):
                chars[res] = val
                res += 1
        i += 1

    return res


