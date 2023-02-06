#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional, List
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: 
        

        def checker(p, q):
            if not p and not q:
                return True
            elif (p and not q) or (not p and q):
                return False
            if p.val != q.val:
                return False
            return True
        
        deque_list = deque([(p,q),])
        while deque_list:
            p,q = deque_list.popleft()
            if not checker(p,q):
                return False
            if q:
                deque_list.append((p.left,q.left))
                deque_list.append((p.right,q.right))
        return True
            
        


# @lc code=end

