class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn,mx_profit = prices[0],0
        for p in prices:
            if p<mn:
                mn = p
            if mx_profit < p-mn:
                mx_profit = p-mn
        return mx_profit