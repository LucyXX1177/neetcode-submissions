class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        all_price=[]
        for i in range(len(prices)):
            curr_price=prices[i]
            for j in range(i+1,len(prices)):
                future_price=prices[j]
                deduce_price=future_price-curr_price 
                all_price.append(deduce_price)
        return max(all_price) if max(all_price) >=0  else 0
        