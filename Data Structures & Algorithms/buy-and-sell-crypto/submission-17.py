class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0 , 1
        max_profit = 0
        while r <= len(prices)-1:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            print(max_profit)
            if prices[l] > prices[r]:
                l+=1
            else:
                r+=1
        return max_profit