#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#

# @lc code=start
from typing import List
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        concats = []
        output = []
        for item in words:
            temp = str(item)
            for i in range(len(words)):
                if words[i] in temp and words[i] != temp:
                    #remove words[i] characters from temp
                    temp = temp.replace(words[i], "")
            if temp == "":
                output.append(temp)
        return output
                    


        


my_solution = Solution()
test_arr = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(my_solution.findAllConcatenatedWordsInADict(test_arr)        )


# @lc code=end

