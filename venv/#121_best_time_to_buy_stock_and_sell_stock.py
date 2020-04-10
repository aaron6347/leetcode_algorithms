"""#121_best_time_to_buy_stock_and_sell_stock.py
    Created by Aaron at 07-Apr-20"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # app1
        # best=0
        # for x in range(len(prices)):
        #     for y in range(x+1, len(prices)):
        #         best=max(prices[y]-prices[x], best)
        # return best

        # app2
        min=10000; best=0
        for x in range(len(prices)):
            if prices[x] < min:
                min=prices[x]
            elif prices[x]-min> best:
                best=prices[x]-min
        return best


run=Solution()
a=[7,1,5,3,6,4,0]
print(run.maxProfit(a))
# app1 brute O(n^2)
# app2 find best O(n)