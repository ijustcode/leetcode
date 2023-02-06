#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:    
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # keep a maximum counter. everytime check the length of path and compare. replace when necessary
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.right, depth+1), dfs(root.left, depth+1))
        return dfs(root, 0)





class ListNode:
    def __init__(self, next = None ):
        self.next = next

def queueChecker(self, person: ListNode):
    person = ListNode()
    count = 0
    if not None:
        #ask the person in front
        queueChecker(person.next)
        pass
    else: 
        return count+1



#         def helper(current_depth: int, left: Optional[TreeNode], right: Optional[TreeNode]) -> int:
#             if not right:
#                 helper(current_depth, left)
#             if not left:
#                 helper(current_depth, right)
#             current_depth += 1
#             return helper(current_depth, left, right)
#         print(root)
#         max_depth = 0
#         if not root:
#             return 0
#         return helper(max_depth, root.left, root.right)

# def inorder(root, res = []):
#     if root:
#         inorder(root.left, res)
#         res.append(root.val)
#         inorder(root.right, res)
#     print(res)
#     return res

# if __name__ == "__main__":

#     my_solution = Solution()


#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.left.left = TreeNode(4)
#     root.left.right = TreeNode(5)

#     print(inorder(root))

        
# @lc code=end



def my_func(person: ListNode) -> int:
    if not person:
        return 1
    else:
        return my_func(person.next)

def maxiDepth(root_node: Optional[TreeNode], depth) -> int:
    
    if not root_node:
        return depth
    else:
        return max(maxiDepth(root_node.right, depth), maxiDepth(root_node.left, depth))

