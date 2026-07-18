class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price,sell_price = 0,0
        maxProfit=0
        while sell_price < len(prices):
            if prices[buy_price] < prices[sell_price]:
                profit=prices[sell_price] - prices[buy_price]
                maxProfit=max(maxProfit,profit)
            else:
                buy_price= sell_price
            sell_price +=1

        return maxProfit    