from typing import List

def rotate(nums: List[int], k: int) -> None:
	"""
	Rotate Array
	Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
	
	Constraints:
	
	1 <= nums.length <= 105
	-231 <= nums[i] <= 231 - 1
	0 <= k <= 105
	
	Follow up:
	"""
	n = len(nums)
	for i in range(k):
		last = nums[0]
		for j in range(n - 2):
			nums[j] = nums[j + 1]
		nums[n - 1] = last
		print(nums)



def test_rotate_array_example_1():
	"""
	Example 1:
	Input:nums = [1,2,3,4,5,6,7], k = 3
	Output:[5,6,7,1,2,3,4]
	Explanation:rotate 1 steps to the right: [7,1,2,3,4,5,6]
	rotate 2 steps to the right: [6,7,1,2,3,4,5]
	rotate 3 steps to the right: [5,6,7,1,2,3,4]
	"""
	output = [5,6,7,1,2,3,4]
	nums = [1, 2, 3, 4, 5, 6, 7]
	k = 3
	rotate(nums, k)
	assert nums == output


def test_rotate_array_example_2():
	"""
	Example 2:
	Input:nums = [-1,-100,3,99], k = 2
	Output:[3,99,-1,-100]
	Explanation:rotate 1 steps to the right: [99,-1,-100,3]
	rotate 2 steps to the right: [3,99,-1,-100]
	"""
	nums = [-1, -100, 3, 99]
	k = 2
	output = [3, 99, -1, -100]
	rotate(nums, k)
	assert nums == output

