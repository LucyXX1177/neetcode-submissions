class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 找到当前步数的之前的最低值 + 找到maximum difference 
        max_profit=0
        min_price=prices[0]
        
        for curr in prices:
            min_price=min(curr,min_price)
            curr_profit=curr-min_price
            max_profit=max(curr_profit,max_profit)
        
        return max_profit
        
        