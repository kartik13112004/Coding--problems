class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or  word.islower() or word[1:].islower() and word[0].isupper():
            return True

        return False
        