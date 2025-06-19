from typing import List


def moveZeroes(nums) -> None:
    """
        Do not return anything, modify nums in-place instead.
        """
    # i - -1, j - non-0
    i = 0
    y = 0
    for j in range(0, len(nums)):
        if nums[j] == 0:
            y += 1
        else:
            nums[i] = nums[j]
            i += 1
        print(nums)
    for j in range(len(nums) - y, len(nums)):
        nums[j] = 0

    print(nums)
