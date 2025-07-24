from typing import List

def maxProfit(prices: List[int]) -> int:
	"""
	Best Time to Buy and Sell Stock
	You are given an array prices where prices[i] is the price of a given stock on the ith day.
	You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
	Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
	
	Constraints:
	
	1 <= prices.length <= 105
	0 <= prices[i] <= 104
	
	"""
	result = 0
	i, j = 0, 1
	while j < len(prices):
		temp =  prices[j] - prices[i]
		if temp > result:
			result = temp
		if prices[i] > prices[j]:
			i = j
		j += 1

	return result


def test_best_time_to_buy_and_sell_stock_example_1():
	"""
	Example 1:
	Input:prices = [7,1,5,3,6,4]
	Output:5
	Explanation:Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
	Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
	"""
	prices = [7,1,5,3,6,4]
	assert maxProfit(prices) == 5


def test_best_time_to_buy_and_sell_stock_example_2():
	"""
	Example 2:
	Input:prices = [7,6,4,3,1]
	Output:0
	Explanation:In this case, no transactions are done and the max profit = 0.
	"""
	prices = [7, 6, 4, 3, 1]
	assert maxProfit(prices) == 0

