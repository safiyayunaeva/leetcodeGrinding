# testing username

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n):
    """
        Given the head of a linked list, remove the nth node from the end of the list
        and return its head.

        It can be solved with 2 pointers when right is shifted by nth elements
    """
    dummy = Node(0, head)
    left = dummy
    right = dummy
    # right is shifted by n
    while n > 0 and right:
        right = right.next
        n = n - 1

    # next step shift both pointers till

    while right:
        left = left.next
        right = right.next

    # when right reaches Null - left is on the node prev to the node we need to delete
    # delete next node
    left.next = left.next.next

    return dummy.next

def sameSubstringDP(s, t, K):
    n = len(s)
    dp = [0] * (n + 1)

    max_len = 0

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + abs(ord(s[i - 1]) - ord(t[i - 1]))

    left = 0
    for right in range(1, n + 1):
        while dp[right] - dp[left] > K:
            left += 1
        max_len = max(max_len, right - left)

    return max_len

from typing import List


def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:
    # create empty list
    intervals.sort(key=lambda i: i[0])
    merged = [intervals[0]]
    print(intervals)

    for start, end in intervals[1:]:
        # getting most recent added interval from merged list
        lastEnd = merged[-1][1]
        if start <= lastEnd:  # intervals overlapping
            # merging - getting max between ending previous interval and ending current
            merged[-1][1] = max(lastEnd, end)
        else:
            merged.append([start, end])
    return merged


print(mergeIntervals([[1, 3], [8, 10], [15, 18], [2, 6], [11, 19]]))


def removeKdigits(num: str, k: int) -> str:
    newL = list(num)
    while k > 0:
        if newL[0] < newL[1]:
            del newL[1]
        else:
            del newL[0]
        k -= 1
    return ''.join(newL)


print(removeKdigits("1432219", 3))

def sortColors( nums: List[int]) -> None:

    def swap(l, r):
        current = nums[r]
        nums[r] = nums[l]
        nums[l] = current

    l = 0
    for r in range(len(nums)):
        if nums[l] > nums[r]:
            swap(l, r)
        if nums[l] == 0:
            l += 1
    print(nums)
    for r in range(l, len(nums)):
        if nums[l] > nums[r]:
            swap(l, r)
        if nums[l] == 1:
            l += 1

    print(nums)
    print(l)

sortColors([2,0,2,1,1,0])
sortColors([2,0,1])