class Solution:
    def varPlay(self,my_list: list) -> None:
        
        print("In the function:                 ", id(my_list))
        my_list.extend([1])
        print("In the function after modif. :   ", id(my_list))
        my_list = my_list + [12,15,17]
        print("In the function after re-ass :   ", id(my_list))
        print(my_list)

if __name__ == "__main__":
    my_solution = Solution()
    my_list = [7,122,199]
    print(my_list)
    print("In the main call:                ", id(my_list))
    my_solution.varPlay(my_list)
    print("the orig. again:                 ", id(my_list))
    
    print(my_list)
    
    
