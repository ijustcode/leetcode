string1 = "abcdef"
string2 = "defghi"
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        intersection = ""
        for i in range(len(strs)-1):
            string1 = strs[i]
            try: 
                string2 = strs[i+1]
            except IndexError:
                "index was out of range for this"
            for i in range(len(string1)):
                if string1[i:] in string2:
                    intersection = string1[i:]
        return intersection
    
    def isItIn(self, string1: str, string2: str) -> str:
        bigger, smaller = (string2, string1) if len(string2) > len(string1) else (string1, string2)
        print(f'bigger is {bigger} and smaller is {smaller}')
        for i in range(len(bigger) - len(smaller) + 1):
            my_expression = bigger[i:i + (len(smaller))]
            print(f'my expression is {my_expression}')
            if smaller == my_expression:
                return True
        return False

    def justFindIt(self, string1: str, string2: str) -> bool:
        bigger, smaller = (string2, string1) if len(string2) > len(string1) else (string1, string2)
        print(f"smaller: {smaller}, bigger: {bigger}")
        if smaller in bigger:
            return True
        else:
            return False

    def find_substrings(self, string: str) -> list:
        substrings = [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]
        return sorted(substrings, key=len, reverse=True)



if __name__ == "__main__":
    my_instance = Solution()
    result = my_instance.justFindIt("something", "thing")
    print(result)
    sub_strings = my_instance.find_substrings("abcdefgh")
    print(sub_strings)



