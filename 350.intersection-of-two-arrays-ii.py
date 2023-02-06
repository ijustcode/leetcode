#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_copy = list(nums1)
        nums2_copy = list(nums2)
        intersection = []
        for i in nums1:
            if i in nums1_copy and i in nums2_copy:
                intersection.append(i)
                nums1_copy.remove(i)
                nums2_copy.remove(i)
        return intersection

        
# @lc code=end

