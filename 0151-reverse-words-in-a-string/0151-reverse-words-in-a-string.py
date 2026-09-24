class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        words.reverse()
        r=" ".join(words)
        return r
      