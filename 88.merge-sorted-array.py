#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start

from typing import Optional
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_counter = m
        for index, elem in enumerate(nums2):
            for j in range(len(nums1)):
                if nums2[index] < nums1[j] or j >= m_counter  :
                    nums1 = nums1[0:j] + [elem] + nums1[j:len(nums1)-1]
                    m_counter += 1
                    break
        print(nums1)


# my_test = Solution()
# my_test.merge([1,2,3,0,0,0],3,[2,5,6],3)
                
        
            


# @lc code=end

