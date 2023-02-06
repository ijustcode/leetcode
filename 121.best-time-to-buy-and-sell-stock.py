#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        minimum = prices[0]
        for i in range(len(prices)):
            minimum = min(minimum, prices[i])
            maximum = max(maximum, prices[i] - minimum)
        return maximum
            
    
            
        
# @lc code=end

