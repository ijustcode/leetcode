class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sub_finder = Solution()
        all_subs = sub_finder.findAllSubarrays(nums)
        total = 0
        overall_sum = 0
        for item in all_subs:
            # print(f'item is: {item}') # and total is: {total}')
            for i in range(len(item)):
                total += item.pop()
            if total % k == 0:
                overall_sum += 1
            total = 0
        return overall_sum


    def findAllSubarrays(self, nums: List[int]):
        subs_ = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                subs_.append(nums[i:j])
        return subs_