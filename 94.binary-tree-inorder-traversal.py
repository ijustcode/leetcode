#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        resolut = []
        resolut = Solution.helper(root, resolut)
        return resolut
    

    def helper(root: TreeNode, res: List) ->  List[int]:
        if root:
            Solution.helper(root.left, res)
            res.append(root.val)
            Solution.helper(root.right, res)
        return res
        
# @lc code=end

