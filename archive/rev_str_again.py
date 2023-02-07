class Solution:
    def __init__(self, length: int = 7) -> None:
        self.length = length

    def reverseString(self, my_str: str) -> str:
        if my_str == "":
            return ""
        else:
            return self.reverseString(my_str[1:])  + my_str[0]



if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.reverseString(input("enter string to be reversed:  ")))

