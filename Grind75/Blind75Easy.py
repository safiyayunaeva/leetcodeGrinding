from typing import List

import pytest


def mergeAlternately(word1: str, word2: str) -> str:
    """
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
    starting with word1. If a string is longer than the other, append the additional letters onto the end
    of the merged string.
    Input: word1 = "abc", word2 = "pqr"
    Output: "apbqcr"
    Input: word1 = "ab", word2 = "pqrs"
    Output: "apbqrs"

    Input: word1 = "abcd", word2 = "pq"
    Output: "apbqcd"
    """
    result = []

    return "".join(result)

@pytest.mark.parametrize(
    "word1,  word2, output",
    [
    ("abc", "pqr", "apbqcr"),
    ("ab", "pqrs", "apbqrs")
])
def test_mergeAlternately( word1,  word2, output):
    result = mergeAlternately(word1, word2)
    assert  result == output


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

