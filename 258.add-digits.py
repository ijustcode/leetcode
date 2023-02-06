#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        # result = 0
        while num % 10 >= 1:
            li_num = [int(x) for x in str(num)]
            total = 0
            for i in li_num:
                total += i
            num = total
            print(num)
        return num
            
        
# @lc code=end

