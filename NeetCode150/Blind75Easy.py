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
    for i in range(max(len(word1),len(word2))):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])

    return "".join(result)

@pytest.mark.parametrize( "word1,  word2, output",
    [
    ("abc", "pqr", "apbqcr"),
    ("ab", "pqrs", "apbqrs"),
    ("abcd", "pq",  "apbqcd")
])
def test_mergeAlternately( word1,  word2, output):
    result = mergeAlternately(word1, word2)
    assert  result == output

def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they
    add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Input: nums = [3,3], target = 6
    Output: [0,1]
    """
    cache = {}
    for index, value in enumerate(nums):
        if value in cache:
            return [cache[value], index]
        cache[target - value] = index
    return [0, 0]

@pytest.mark.parametrize( "nums,  target, output",
    [
    ([2,7,11,15], 9, [0,1]),
    ([3,2,4], 6, [1,2]),
    ([3,3], 6,  [0,1])
])
def test_twoSum(nums, target, output):
    result = twoSum(nums, target)
    assert result == output