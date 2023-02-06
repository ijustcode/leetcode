#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # define a loop with numRows iterations
        # in each iteration
        #           create empty list                   
        #           fill it with numbers based on element before
        all_rows = []
        for j in range(numRows):
            if j == 0:
                all_rows.append([1])
            elif j == 1:
                all_rows.append([1,1]) 
            else:
                row = []
                for i in range(j+1):
                    if i == 0 or i == j:
                        row.append(1)
                    else:
                        row.append(all_rows[j-1][i-1] + all_rows[j-1][i])
                all_rows.append(row)
        return all_rows



# if __name__ == "__main__":
#     my_solution = Solution()
#     print(my_solution.generate(int(input())))
            
                       
# @lc code=end

