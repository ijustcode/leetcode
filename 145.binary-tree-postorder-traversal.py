#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node_vals = []
        node_vals = Solution.traverse_postorder(node_vals, root)
        return node_vals        
        
    def traverse_postorder(my_l: List, rt: TreeNode) -> List:
        if rt:
            Solution.traverse_postorder(my_l, rt.left)
            Solution.traverse_postorder(my_l, rt.right)
            my_l.append(rt.val)
        return my_l


# @lc code=end

