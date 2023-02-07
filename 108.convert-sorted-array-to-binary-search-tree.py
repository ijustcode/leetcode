#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid_point = int(len(nums) / 2)
        mid_value = nums[mid_point]        
        root = TreeNode(val=mid_value)
        right_side = nums[:mid_point]
        left_side = nums[mid_point+1:]
        right_side.reverse()
        left_side.reverse()
        while right_side and left_side:
            #add every right side value to right
            #add every left side value to left
            pass
        #maybe do it recursively
        return root



# @lc code=end

