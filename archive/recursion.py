# This function reverses a string. Using recursion.
import sys

class Solution:

    def __init__(self, height: int = 2) -> None:
        self.height = height

    def reverseString(self, word: str) -> str:
        if word == '':
            return ''
        return self.reverseString(word[1:]) + word[0]
    
    def decToBinary(self, dec: int, all_outs: str) -> str:
        if dec == 0:
            return all_outs
        all_outs = str(dec % 2) + all_outs
        return self.decToBinary(int(dec / 2), all_outs)

if __name__ == "__main__":

    com_line_args = sys.argv
    my_solution = Solution(17)
    if com_line_args[1] == '1':            
        word = input("Enter your word: ")
        my_var = my_solution.reverseString(word)
        print(my_var)
        print(type(my_solution.height))
        print(my_solution.height)
    if com_line_args[1] == '2':
        print("all of arguments: ", str(sys.argv[1]))
    if com_line_args[1] == '3':
        print(my_solution.decToBinary(233, ""))