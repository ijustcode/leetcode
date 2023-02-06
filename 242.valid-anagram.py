#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = [x for x in s]
        t_list = [y for y in t]
        for x in s:
            if x in t_list and x in s_list:
                try:
                    s_list.remove(x) 
                    t_list.remove(x)
                except:
                    return False
            else:
                return False
        if s_list or t_list:
            return False
        else: 
            return True
            

# my_solution = Solution()
# print(my_solution.isAnagram("anagram", "nagaram"))
        
# @lc code=end

