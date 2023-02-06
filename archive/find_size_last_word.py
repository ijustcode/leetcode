class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        indiv_words = s.strip()
        indiv_words = indiv_words.split(" ")
        indiv_words = indiv_words[-1]
        return len(indiv_words)

if __name__ == "__main__":
    big_word_finder = Solution()
    big_word = big_word_finder.lengthOfLastWord("hello from uzbakistan!")
    print(big_word) 