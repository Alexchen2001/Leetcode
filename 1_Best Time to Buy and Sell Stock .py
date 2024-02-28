class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ## initiate a two pointer 
        low = 0
        high = 1

        ## result: no profit
        maxProfit = 0

        ## this while loop makes sure that it does not exceed the bound
        while high < len(prices):
            ##Checks the current price 
            currProfit = prices[high] - prices[low]
            ## compares whether if price of low is  lower 
            ## if not then it initate the new low in the else
            ## if it is lower it checks whether if the Profit is maximized
            if prices[low] < prices[high]:
                maxProfit = max(maxProfit, currProfit)
            else:
                low = high

            ## increment the index of array
            high += 1
        return maxProfit