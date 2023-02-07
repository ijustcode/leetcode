import sys
class Solution:
    def __init__(self) -> None:
        pass

    def recursiveAdder(self, num: int, result = 0) -> int:
        if num == 0:
            return result
        else:
            return self.recursiveAdder(num-1, result + num)

    def binarySearch(self, arr: list, start, end, target: int) -> int:
        mid_point = int((start + end) / 2)
        if arr[mid_point] == target:
            return mid_point
        elif arr[mid_point] > target:
            return self.binarySearch(arr,0, mid_point, target)
        return self.binarySearch(arr, mid_point + 1, len(arr) -1 , target)

if __name__ == "__main__":
    my_solution = Solution()
    if sys.argv[1] == "1":
        print(my_solution.recursiveAdder(int(input("enter some number: ", ))))
    elif sys.argv[1] == "2":
        my_array = [-1, 0, 1, 2, 3, 4, 7, 9, 10, 20]
        my_target = int(input("enter the target: ... "))
        print(my_solution.binarySearch(my_array, 0, len(my_array)-1, my_target))