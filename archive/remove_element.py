from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for ind, item in enumerate(nums):
            if item == val:
                nums[ind] = '_'
            if ind > 1:
                if nums[ind - 1] == '_':
                    temp = nums[ind]
                    nums[ind] = '_'
                    nums[ind - 1] = temp
        for i in range(len(nums)-1,-1,-1):
            if nums[i] != '_':
                return len(nums)-i
                
                return(something)

                