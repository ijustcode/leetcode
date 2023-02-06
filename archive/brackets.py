class Solutions:
    def isValid(self, s: str) -> bool:
        order = True
        pairs = {'(': ')', '{': '}', '[': ']'}
        str_list = []
        for i in range(len(s)-1,-1,-1):
            str_list.append(s[i])
        print(str_list)

        for ind in range(len(str_list)):
            str_list.pop()
        # now popping and evaluating:
        dummy = []
        for i in range(len(str_list)):
            temp = str_list.pop()
            if dummy is None or dummy.pop() == pairs[temp]:
                order = True
            else:
                order = False

            if order == False:
                return order
        return True





if __name__ == "__main__":
    bracket_checker = Solutions()
    bracket_checker.isValid("()[]{}")
    