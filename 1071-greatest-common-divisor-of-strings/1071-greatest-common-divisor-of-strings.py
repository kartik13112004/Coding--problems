class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        import math
        k=math.gcd(len(str1),len(str2))
        length=str1[:k]
        if (str1==length*(len(str1)//len(length))) and  (str2==length*(len(str2)//len(length))):
            return length
        return ""
  
  
        