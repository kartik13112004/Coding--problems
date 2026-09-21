class Solution:
    def firstUniqChar(self, s: str) -> int:
        k=s[0]
        for i in range (len(s)):
            if s.count(s[i])==1:
                return i
                break
        else:
            return -1
        