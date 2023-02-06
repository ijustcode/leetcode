#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # at each given point must: lft subtree == rt subtree        
        # deq = deque()
        # deq.append(root)
        def isMirror(right, left):
            if not right and not left:
                return True
            if not right or not left:
                return False
            if right.val != left.val:
                return False
            if right and left:
                if isMirror(right.left, left.right) and isMirror(right.right, left.left):
                    return True
            return False            
        if not root:
            return True
        else:
            return isMirror(root.right, root.left)
            

# @lc code=end

