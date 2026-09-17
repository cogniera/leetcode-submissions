#Author Name : Paarth Sharma
#File Name : bestTimeStock.py
#Project Name : leetcode-submissions
#Creation Date : 16th September 2026
#Desc : find's the best days to buy and sell a stock and make the highest profit 
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        L = 0
        profit = 0 

        for R in range(len(prices)):
            if prices[L] < prices[R]:
                profit = max(profit, prices[R] - prices[L])
            else:
                L = R
            
        return profit
#Time Complexity : O(n)
#Space Complexity : O(1)
#Time : 51ms Beats 51.53%
#Space : 28.77MB Beats 21.72%
