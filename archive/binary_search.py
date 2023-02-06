from typing import List
class Solutions:
    def __init__(self) -> None:
        pass
        
    def binarySearch(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        mid = int((low + high ) / 2)
        while high >= low:
            print(f'high: {high} low: {low} mid_point: {mid} target {target}')
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
                mid = int((low + high)/2)
            elif nums[mid] < target:
                low = mid + 1
                mid = int((low + high) / 2)
        return -1


if __name__ == "__main__":
    my_arr = [3,5,8,11,17,25]
    tar = 8
    my_sol = Solutions()
    print(my_sol.binarySearch(my_arr,tar))

        