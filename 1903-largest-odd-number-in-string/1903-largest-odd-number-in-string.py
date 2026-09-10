class Solution:
    def largestOddNumber(self, num: str) -> str:
        if num[-1] in "13579":
            return num
        else:
            for i in range(len(num) - 1, -1, -1):
                if num[i] in "13579":
                    return num[:i+1]
            return ""