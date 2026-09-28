class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        word1="".join(word1)
        word2="".join(word2)
        if word1==word2:
            return True
        return False
        